#!/usr/bin/env python3
"""
Run the FastAPI server for the UNF Tour Guide

Make sure Ollama is running first:
    ollama serve

Then run this script:
    python run_api.py

The web interface will be available at http://localhost:8000
"""

import uvicorn

if __name__ == "__main__":
    print("=" * 60)
    print("UNF Tour Guide API Server")
    print("=" * 60)
    print("\nStarting server on http://localhost:8000")
    print("Press Ctrl+C to stop the server\n")
    
    uvicorn.run(
        "api:app",
        host="0.0.0.0",
        port=8000,
        reload=True,  # Auto-reload on code changes
        log_level="info"
    )
