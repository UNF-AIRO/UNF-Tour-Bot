import ollama
import torch

# Configuration
MODEL = "Mistral"

# Check if GPU is available
def detect_gpu():
    gpu_available = torch.cuda.is_available()
    if gpu_available:
        gpu_count = torch.cuda.device_count()
        gpu_name = torch.cuda.get_device_name(0)
        print(f"GPU detected: {gpu_name} ({gpu_count} device(s))")
        # Return options to use GPU
        return True, {
            "num_gpu": gpu_count,    # Use all available GPUs
            "main_gpu": 0,           # Use first GPU as main
        }
    else:
        print("No GPU detected, using CPU")
        return False, {}

GPU_AVAILABLE, GPU_OPTIONS = detect_gpu()

def get_system_prompt(building_number) -> str:
    try:
        with open(str(building_number) + ".txt", "r") as file:
            info = file.read()
    except FileNotFoundError:
        print(f"Warning: Building file {building_number}.txt not found")
        info = "No building information available."

    SYSTEM_PROMPT = f"""You are a helpful tour guide for the University of North Florida (UNF). 
    You provide information about campus locations, buildings, facilities, and general tour guidance. 
    Be friendly, informative, and concise in your responses.

    Here is the UNF campus information you should reference:
    {info}

    Use this information to answer questions about UNF accurately."""
    return SYSTEM_PROMPT


def chat_with_tour_guide(user_message: str, building_number):
    try:
        response = ollama.chat(
            model=MODEL,
            messages=[
                {
                    "role": "system",
                    "content": get_system_prompt(building_number = building_number)
                },
                {
                    "role": "user",
                    "content": user_message
                }
            ],
            stream=False,
            options=GPU_OPTIONS  # Pass GPU options if available
        )
        
        return response["message"]["content"]
    
    except Exception as e:
        return f"Error: {str(e)}. Please make sure Ollama is running on localhost:11434"


if __name__ == "__main__":
    print("=" * 60)
    print("UNF Tour Guide Chatbot")
    print("=" * 60)
    print("Type 'quit' or 'exit' to end the conversation")
    print("Type 'building <number>' to change buildings\n")
    
    building_number = int(input("Enter current building number: "))

    while True:
        user_input = input("You: ").strip()
        
        if user_input.lower() in ["quit", "exit", "q"]:
            print("Thank you for using the UNF Tour Guide. Goodbye!")
            break
        
        # Check if user wants to change building
        if user_input.lower().startswith("building "):
            try:
                new_building = int(user_input.split()[1])
                building_number = new_building
                print(f"Switched to building {building_number}.\n")
                continue
            except (IndexError, ValueError):
                print("Invalid format. Use 'building <number>' to change buildings.\n")
                continue
        
        if not user_input:
            continue
        
        print("\nTour Guide: ", end="", flush=True)
        response = chat_with_tour_guide(user_input, building_number=building_number)
        print(response)
        print()