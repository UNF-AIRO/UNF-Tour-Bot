# Running the UNF Tour Guide with Web Interface

## Quick Start

### Step 1: Start Ollama Service
Open a PowerShell terminal and run:
```powershell
ollama serve
```
Leave this running in the background. You should see "Listening on localhost:11434"

### Step 2: Activate Virtual Environment & Run API Server
Open a new PowerShell terminal in the project directory:
```powershell
& "tour_bot\Scripts\Activate.ps1"
python run_api.py
```

The API server will start on `http://localhost:8000`

### Step 3: Open in Browser
Open your browser and navigate to:
```
http://localhost:8000
```

You should see the UNF Tour Guide web interface!

## Features

- **Web-based Chat Interface**: Beautiful, responsive chat UI
- **Building Selection**: Choose from available buildings in the sidebar
- **Real-time Chat**: Stream messages back and forth with the tour guide
- **Auto-scroll**: Messages automatically scroll into view
- **Mobile Friendly**: Responsive design works on tablets and phones

## API Endpoints

If you want to build your own frontend or integrate with other apps, use these JSON endpoints:

### Get Available Buildings
```
GET /api/buildings
```
Response:
```json
{
  "buildings": ["15", "2", "43", "45", "50", "57"]
}
```

### Get Building Info
```
GET /api/building/{building_id}
```
Response:
```json
{
  "building_number": "15",
  "info": "Building information text..."
}
```

### Send Chat Message
```
POST /api/chat
Content-Type: application/json

{
  "message": "Where is the library?",
  "building": "15",
  "chat_history": []
}
```

Response:
```json
{
  "message": "The library is located on the east side of the campus...",
  "building": "15",
  "chat_history": [
    {"role": "user", "content": "Where is the library?"},
    {"role": "assistant", "content": "The library is located on the east side..."}
  ]
}
```

### Reset Session
```
POST /api/reset-session/{building_id}
```

## Troubleshooting

**"Connection refused" on http://localhost:8000**
- Make sure you ran `python run_api.py` in the correct terminal
- Check that the API server started successfully

**"Please make sure Ollama is running" error**
- Make sure you have `ollama serve` running in another terminal
- Verify it's listening on localhost:11434

**Building not showing up**
- Make sure `.txt` files are in the `building_info/` folder
- Reload the page to refresh the building list
