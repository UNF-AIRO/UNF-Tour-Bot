# UNF Tour Guide Chatbot

A conversational AI chatbot that provides information about the University of North Florida campus, locations, buildings, and facilities.

## Prerequisites

- Python 3.x installed
- Ollama installed ([Download here](https://ollama.ai))

## Models

- **Testing**: Mistral (lightweight, fast iteration)
- **Deployment**: Llama2 (more capable, production-ready)

## Setup (First Time Only)

1. **Install Python packages:**
   ```
   pip install -r requirements.txt
   ```
   Or manually install: `pip install ollama pydantic torch`

---

## Running the Chatbot - Main Method

*(Coming soon - model training in progress)*

---

## Running the Chatbot - Testing Method

### Prerequisites for Testing

- The Mistral model downloaded:
  ```
  ollama pull mistral
  ```
  This downloads the AI model (~4GB). Only do this once.

### Step 1: Start Ollama Service
Open a PowerShell terminal and run:
```powershell
ollama serve
```
Leave this running in the background. You should see "Listening on localhost:11434"

### Step 2: Run the Testing Chatbot
Open a new PowerShell terminal and run:
```powershell
& "tour_bot\Scripts\Activate.ps1"
python testing-chat-bot.py
```

The chatbot will start and display:
```
============================================================
UNF Tour Guide Chatbot
============================================================
Type 'quit' or 'exit' to end the conversation
Type 'building <number>' to change buildings
```

### Using the Testing Chatbot

- Type your questions about UNF campus
- Examples:
  - "Where is the library?"
  - "Tell me about the student center"
  - "How do I get to the engineering building?"
- The bot will respond with helpful information and maintain conversation history
- Type `building <number>` to switch buildings (this resets conversation history)
- Type `quit`, `exit`, or `q` to end the conversation

### Features

- **Conversation Memory**: The bot maintains chat history within each building session for more natural conversations
- **Building Context**: Each building has its own information file for specific details
- **CPU/GPU Support**: Automatically detects and uses GPU if available (configurable with `FORCE_CPU` flag)

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

**GPU Not Being Used**
- Check with `nvidia-smi` to verify your NVIDIA drivers are installed
- Install PyTorch with CUDA support: `pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121`
- Set `FORCE_CPU = False` in `testing-chat-bot.py`

## Notes

- Ollama must be running continuously while you use the chatbot
- You only need to pull the model once
- Running both Ollama and the chatbot in separate terminals keeps them responsive
- The testing chatbot is set up specifically for UNF campus information
