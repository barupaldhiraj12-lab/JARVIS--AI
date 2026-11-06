# JARVIS--AI
Personal Ai
import datetime

def jarvis():
    print("JARVIS AI STARTED")

    print("Hello! I am Jarvis.")

    while True:
        command = input("You: ").lower()

        if "hello" in command:
            print("Jarvis: Hello! How are you?")

        elif "time" in command:
            now = datetime.datetime.now()
            print("Jarvis:", now.strftime("%I:%M %p"))

        elif "date" in command:
            today = datetime.date.today()
            print("Jarvis:", today)

        elif "નમસ્તે" in command:
            print("Jarvis: નમસ્તે! કેમ છો?")

        elif "બંધ" in command or "exit" in command:
            print("Jarvis: Goodbye!")
            break

        else:
            print("Jarvis: I am learning!")

jarvis()
