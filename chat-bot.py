import ollama
import os

# Configuration
MODEL = "mistral"

# Load UNF information from file
def load_unf_info():
    info_file = "UNF_INFO.txt"
    if os.path.exists(info_file):
        with open(info_file, 'r') as f:
            return f.read()
    else:
        return "No UNF information file found. Make sure UNF_INFO.txt exists in the same directory."

UNF_INFO = load_unf_info()

SYSTEM_PROMPT = f"""You are a helpful tour guide for the University of North Florida (UNF). 
You provide information about campus locations, buildings, facilities, and general tour guidance. 
Be friendly, informative, and concise in your responses.

Here is the UNF campus information you should reference:

{UNF_INFO}

Use this information to answer questions about UNF accurately."""


def chat_with_tour_guide(user_message: str) -> str:
    try:
        response = ollama.chat(
            model=MODEL,
            messages=[
                {
                    "role": "system",
                    "content": SYSTEM_PROMPT
                },
                {
                    "role": "user",
                    "content": user_message
                }
            ],
            stream=False
        )
        
        return response["message"]["content"]
    
    except Exception as e:
        return f"Error: {str(e)}. Please make sure Ollama is running on localhost:11434"


if __name__ == "__main__":
    print("=" * 60)
    print("UNF Tour Guide Chatbot")
    print("=" * 60)
    print("Type 'quit' or 'exit' to end the conversation\n")
    
    while True:
        user_input = input("You: ").strip()
        
        if user_input.lower() in ["quit", "exit", "q"]:
            print("Thank you for using the UNF Tour Guide. Goodbye!")
            break
        
        if not user_input:
            continue
        
        print("\nTour Guide: ", end="", flush=True)
        response = chat_with_tour_guide(user_input)
        print(response)
        print()
