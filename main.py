from app.llm import call_llm

def chatbot():
    print("GPT-4o CLI Chatbot for Math operations")
    print("Type 'exit' to quit.")
    while True:
        query = input("You: ")
        if query.lower() == "exit":
            print("Ending session with chatbot!")
            break
        try:
            response = call_llm(query)
            print(f"Bot: {response} \n")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    chatbot()