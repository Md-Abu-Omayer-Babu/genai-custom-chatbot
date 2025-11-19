from llm_client import get_model


def main():
    model = get_model()
    chat = model.start_chat()

    print("Islamic Perspective Generator (type 'exit' to quit)\n")

    while True:
        topic = input("Ask anything about Islam: ")

        if topic.lower() in ["exit", "quit"]:
            break

        prompt = (
            f"Provide a short Islamic perspective on: {topic}. "
            f"Include authentic references from Qur'an or Sahih Hadith."
        )

        response = chat.send_message(prompt)
        print("\nResponse:\n", response.text, "\n")


if __name__ == "__main__":
    main()
