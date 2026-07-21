from responses import get_response

print("=" * 50)
print("              RULE-BASED CHATBOT")
print("=" * 50)
print("Type 'bye' to exit.\n")

while True:

    user_input = input("You : ")

    if user_input.lower() == "bye":
        print("Bot : Goodbye! Have a nice day.")
        break

    response = get_response(user_input)

    print("Bot :", response)