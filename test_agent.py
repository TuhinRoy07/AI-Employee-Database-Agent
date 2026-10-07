from agent import ask_agent

while True:

    question = input("\nYou: ")

    if question.lower() == "exit":
        break

    answer = ask_agent(
        question
    )

    print(
        "\nAI:",
        answer
    )