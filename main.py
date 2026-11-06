import datetime

print("JARVIS AI STARTED")
print("નમસ્તે! હું તમારો Jarvis છું.")

while True:
    command = input("You: ").lower()

    if "hello" in command:
        print("Jarvis: Hello! How are you?")

    elif "નમસ્તે" in command:
        print("Jarvis: નમસ્તે! કેમ છો?")

    elif "time" in command:
        print(datetime.datetime.now().strftime("%I:%M %p"))

    elif "date" in command:
        print(datetime.date.today())

    elif "exit" in command or "બંધ" in command:
        print("Jarvis: Goodbye!")
        break

    else:
        print("Jarvis: I am learning!")
