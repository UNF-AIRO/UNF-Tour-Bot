import uvicorn
from api import app

if __name__ == "__main__":
    print("=" * 60)
    print("Starting UNF Tour Guide API Server")
    print("=" * 60)
    print("Server running at: http://localhost:8000")
    print("OpenAPI docs at: http://localhost:8000/docs")
    print("=" * 60)
    
    uvicorn.run(app, host="0.0.0.0", port=8000)