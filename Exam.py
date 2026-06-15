class Exam:
    __Exam_name = "JEE MAINS"

    def __init__(self, name, ID, standard):
        self.__name=name
        self.__ID=ID
        self.standard=standard

    def get_name(self):
        return self.__name
    
    def set_change_name(self, new_name):
         if type(new_name) == str:  
            self.__name = new_name
            print(f"name is updated to {new_name}")
         else:
            raise Exception("Name must be a string!") 

    @staticmethod
    def get_exam_name():
        return Exam.__Exam_name

    def __str__(self):
        return f"Student: {self.__name}, ID: {self.__ID}, Standard: {self.standard}"

student=Exam("Tanmay",67,10)
print(student)

print(Exam.get_exam_name())  


print(student.get_name())

student.set_change_name("Rahul")
print(student.get_name())






