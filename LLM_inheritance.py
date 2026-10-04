class LLM:

    def __init__(self, name):
        self.name = name

    def intro(self):
        return f"Welcome to your personal LLM {self.name}"
    
    def start(self):
        return "Let's get you started"

    def model_info(self):
        return f"{self.name} is ready to assist you."

    def ask(self, question):
        return f"You asked: {question}"


obj = LLM("Tanmay")

print(obj.intro())
print(obj.start())
print(obj.model_info())
print(obj.ask("What is Python?"))
