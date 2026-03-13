import ollama
from file_reader import read_building_info

# Configuration
MODEL = "Mistral"  # Production model: llama2, Testing model: Mistral

def get_system_prompt(building_number: str) -> str:
    """Generate system prompt with building-specific information."""
    building_info = read_building_info(building_number)
    
    if building_info is None:
        building_info = f"No specific information available for building {building_number}."
    
    return f"""You are a friendly and knowledgeable tour guide for the University of North Florida (UNF). 
Your role is to help visitors and students navigate the campus and learn about campus facilities and services.
Be warm, welcoming, and provide helpful information about UNF locations, buildings, and services.
Keep your responses concise and natural, as if you're speaking to someone in person.

Building {building_number} Information:
{building_info}

Use this information to answer questions about this building and provide context about UNF campus.
If asked about other buildings or areas, offer to help them navigate to those locations."""


def chat_with_tour_guide(user_message: str, building_number: str, chat_history: list) -> str:
    """Get response from tour guide chatbot."""
    try:
        # Add user message to history
        chat_history.append({"role": "user", "content": user_message})
        
        # Build messages with system prompt
        messages = [{"role": "system", "content": get_system_prompt(building_number)}]
        messages.extend(chat_history)
        
        response = ollama.chat(model=MODEL, messages=messages, stream=False)
        assistant_message = response["message"]["content"]
        
        # Add assistant response to history
        chat_history.append({"role": "assistant", "content": assistant_message})
        
        return assistant_message
    except Exception as e:
        return f"Error: {str(e)}. Please ensure Ollama is running on localhost:11434"
