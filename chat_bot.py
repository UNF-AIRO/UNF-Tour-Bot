import ollama
from file_reader import read_building_info, get_available_buildings

# Configuration
MODEL = "Mistral"  # Production model llama2, testing model Mistral
FORCE_CPU = True  # Set to True to use CPU only, False to use GPU if available

def get_system_prompt(building_number: str) -> str:

    building_info = read_building_info(building_number)
    
    if building_info is None:
        building_info = f"No specific information available for building {building_number}."
    
    SYSTEM_PROMPT = f"""You are a friendly and knowledgeable tour guide for the University of North Florida (UNF). 
Your role is to help visitors and students navigate the campus and learn about campus facilities and services.
Be warm, welcoming, and provide helpful information about UNF locations, buildings, and services.
Keep your responses concise and natural, as if you're speaking to someone in person.

Here is the specific information about the building you're currently at (Building {building_number}):
{building_info}

Use this information to answer questions about this building and provide context about UNF campus.
If asked about other buildings or areas, offer to help them navigate to those locations."""
    
    return SYSTEM_PROMPT


def chat_with_tour_guide(user_message: str, building_number: str, chat_history: list) -> str:
    try:
        # Add user message to history
        chat_history.append({
            "role": "user",
            "content": user_message
        })
        
        # Build messages list with system prompt first, then history
        messages = [
            {
                "role": "system",
                "content": get_system_prompt(building_number)
            }
        ]
        messages.extend(chat_history)
        
        response = ollama.chat(
            model=MODEL,
            messages=messages,
            stream=False
        )
        
        assistant_message = response["message"]["content"]
        
        # Add assistant response to history
        chat_history.append({
            "role": "assistant",
            "content": assistant_message
        })
        
        return assistant_message
    
    except Exception as e:
        return f"Error: {str(e)}. Please make sure Ollama is running on localhost:11434"


def start():
    # Get initial building
    available_buildings = get_available_buildings()
    
    if not available_buildings:
        print("Warning: No building files found in building_info/")
        print("Please create building information files before using the tour guide.\n")
    
    while True:
        building_number = input("Enter current building number (or 'list' to see available): ").strip()
        
        if building_number.lower() == 'list':
            if available_buildings:
                print(f"Available buildings: {', '.join(available_buildings)}\n")
            else:
                print("No buildings available yet.\n")
            continue
        
        if building_number and building_number not in available_buildings:
            print(f"Warning: Building {building_number} not found, but continuing anyway.\n")
        elif building_number:
            break
    
    chat_history = []
    
    print(f"\nStarting tour at Building {building_number}")
    print("Tour Guide: Hello! Welcome to Building " + building_number + ". Ask me anything about this building or the campus!\n")
    
    while True:
        user_input = input("You: ").strip()
        
        if user_input.lower() in ["quit", "exit", "q"]:
            print("\nTour Guide: Thank you for joining the tour! Have a great day at UNF!")
            break
        
        # Check if user wants to change building
        if user_input.lower().startswith("building "):
            try:
                new_building = user_input.split(maxsplit=1)[1]
                building_number = new_building
                chat_history = []  # Reset conversation history when changing buildings
                print(f"\nSwitched to building {building_number}. Starting fresh conversation.\n")
                continue
            except (IndexError, ValueError):
                print("Invalid format. Use 'building <number>' to change buildings.\n")
                continue
        
        # Check for list command
        if user_input.lower() == "list":
            if available_buildings:
                print(f"Available buildings: {', '.join(available_buildings)}\n")
            else:
                print("No buildings available.\n")
            continue
        
        if not user_input:
            continue
        
        print("\nTour Guide: ", end="", flush=True)
        response = chat_with_tour_guide(user_input, building_number=building_number, chat_history=chat_history)
        print(response)
        print()