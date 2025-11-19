from llm_client import get_model

def main():
    model = get_model()
    
    chat = model.start_chat(history=[])

    print("Custom Gemini Chatbot (type 'exit' to quit)\n")

    while True:
        user_input = input("Ask Anything: ")

        if user_input.lower() in ["exit", "quit"]:
            print("Goodbye!")
            break
        
        response = chat.send_message(user_input)
        print("Gemini:", response.text)

if __name__ == "__main__":
    main()