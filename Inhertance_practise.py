class Job:

    def __init__ (self,name,title,salary):
        self.name=name
        self.title=title
        self.salary=salary
        self.resume=None

    print("Welcome to job applying portal")

    def __str__(self):
        return f"My name is {self.name}. I am an {self.title} and my current salary is {self.salary}."
    
    def upload_resume(self,file_path):
        self.resume=file_path
        print(f" Resume uploaded for {self.name}: {file_path}")



obj=Job("Tanmay","AI enginerr",50000)
obj.upload_resume("C:/Users/tanmay/resume.pdf")
print(obj)
print(obj.resume)