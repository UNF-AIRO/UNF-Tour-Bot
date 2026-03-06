# UNF Tour Guide Chatbot

A conversational AI chatbot that provides information about the University of North Florida campus, locations, buildings, and facilities.

## Prerequisites

- Python 3.x installed
- Ollama installed ([Download here](https://ollama.ai))
- The Mistral model downloaded

## Setup (First Time Only)

1. **Install Python packages:**
   ```
   pip install -r requirements.txt
   ```
   Or manually install: `pip install ollama pydantic`

2. **Download the Mistral model:**
   ```
   ollama pull mistral
   ```
   This downloads the AI model (~4GB). Only do this once.

## How to Run the Bot

### Step 1: Start Ollama Service
Open a PowerShell terminal and run:
```
ollama serve
```
Leave this running in the background. You should see "Listening on localhost:11434"

### Step 2: Run the Chatbot
Open a new PowerShell terminal and run:
```
& "tourbot\Scripts\Activate.ps1"
python chat-bot.py
```

The chatbot will start and display:
```
============================================================
UNF Tour Guide Chatbot
============================================================
Type 'quit' or 'exit' to end the conversation
```

## Using the Chatbot

- Type your questions about UNF campus
- Examples:
  - "Where is the library?"
  - "Tell me about the student center"
  - "How do I get to the engineering building?"
- The bot will respond with helpful information
- Type `quit`, `exit`, or `q` to end the conversation

## Quick Start Batch File

Save this as `run-bot.bat` in your project folder for convenience:

```batch
@echo off
start ollama serve
timeout /t 3
cd /d "%~dp0"
cmd /k & "tourbot\Scripts\Activate.ps1" && python chat-bot.py
```

Then just double-click `run-bot.bat` to start everything!

## Troubleshooting

**"Error: Please make sure Ollama is running"**
- Make sure you have `ollama serve` running in another terminal
- Check that it's listening on localhost:11434

**"Model not found" error**
- Run `ollama pull mistral` to download the model

**Slow responses**
- First query with Mistral takes longer to load
- Subsequent queries will be faster
- This is normal behavior

## Notes

- Ollama must be running continuously while you use the chatbot
- You only need to pull the model once
- Running both Ollama and the chatbot in separate terminals keeps them responsive
- The chatbot is set up specifically for UNF campus information
