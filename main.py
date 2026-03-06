import web_search
import chat_bot as ozzie
import file_reader

if __name__ == "__main__":
    print("=" * 60)
    print("Welcome to UNF Tour Guide")
    print("=" * 60)
    print("Type 'quit' or 'exit' to end the conversation")
    print("Type 'building <number>' to change buildings")
    print("Type 'list' to see available buildings\n")

    ozzie.start()