class LLM:

    def __init__(self,name):
        self.name=name


    def intro(self):
        return f"Welcome to your personal LLM {self.name}"
    
   

obj=LLM("Tanmay")
print(obj.intro())
