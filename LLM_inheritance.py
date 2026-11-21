
class LLM:

    def __init__(self, name):
        self.name = name
        self.history = []

    def intro(self):
        return f"Welcome to your personal LLM {self.name}"

    def start(self):
        return "Let's get you started"

    def model_info(self):
        return f"{self.name} is ready to assist you."

    def ask(self, question):
        self.history.append(question)
        return f"You asked: {question}"

    def show_history(self):
        return self.history


obj = LLM("Tanmay")

print(obj.intro())
print(obj.start())
print(obj.model_info())

print(obj.ask("What is Python?"))
print(obj.ask("What is Machine Learning?"))

print(obj.show_history())
