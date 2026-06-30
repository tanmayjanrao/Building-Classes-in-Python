class LLM:

    def __init__(self,name):
        self.name=name


    def intro(self):
        return f"Welcome to your personal LLM {self.name}"
    
    def start(self):
        return "Let's get you started"


obj=LLM("Tanmay")
print(obj.intro())
print(obj.start())
