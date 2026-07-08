("My-Jarvis AI Starting...")print("My-Jarvis AI Starting...")

name = input("Your name: ")
print("Hello,", name)
question = input("Ask me anything: ")

if "hello" in question.lower():
    print("Hello! How can I help you?")
elif "your name" in question.lower():
    print("I am My-Jarvis AI.")
else:
    print("Sorry, I'm still learning.")