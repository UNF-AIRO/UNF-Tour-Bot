from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
import os

import chat_bot
from file_reader import get_available_buildings, read_building_info
from api_models import ChatRequest, ChatResponse, BuildingResponse, BuildingInfoResponse

app = FastAPI(title="UNF Tour Guide API", version="1.0.0")

# Enable CORS for cross-origin requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Store chat histories per session
chat_sessions = {}

@app.get("/api/buildings", response_model=BuildingResponse)
def get_buildings():
    """Get list of all available buildings"""
    buildings = get_available_buildings()
    return BuildingResponse(buildings=buildings)

@app.get("/api/building/{building_id}", response_model=BuildingInfoResponse)
def get_building_info(building_id: str):
    """Get information about a specific building"""
    info = read_building_info(building_id)
    if info is None:
        raise HTTPException(status_code=404, detail=f"Building {building_id} not found")
    return BuildingInfoResponse(building_number=building_id, info=info)

@app.post("/api/chat", response_model=ChatResponse)
def chat(request: ChatRequest):
    """Send a message to the tour guide and get a response"""
    try:
        # Get or create chat history for this building
        if request.building not in chat_sessions:
            chat_sessions[request.building] = []
        
        # Use provided history or stored session history
        chat_history = request.chat_history if request.chat_history else chat_sessions[request.building]
        
        response = chat_bot.chat_with_tour_guide(
            request.message,
            request.building,
            chat_history
        )
        
        # Update stored history
        chat_sessions[request.building] = chat_history
        
        return ChatResponse(
            message=response,
            building=request.building,
            chat_history=chat_history
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/api/reset-session/{building_id}")
def reset_session(building_id: str):
    """Reset chat history for a building"""
    if building_id in chat_sessions:
        del chat_sessions[building_id]
    return {"status": "success", "building": building_id}

@app.get("/")
def read_root():
    """Serve the web interface"""
    return FileResponse("static/index.html")

# Serve static files (CSS, JS, etc.)
if os.path.exists("static"):
    app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/health")
def health_check():
    """Health check endpoint"""
    return {"status": "healthy"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
