class Vehicle:

    vehicle_count=0

    def __init__(self,brand,model,year,num_wheels):
        self.__brand=brand
        self.__model=model
        self.__year=year
        self.__num_wheels=num_wheels

    ## getter methods
    def get_brand(self):
        return self.__brand
    
    def get_model(self):
        return self.__model
    
    def get_year(self):
        return self.__year  
    
    def get_num_wheels(self):
        return self.__num_wheels
    
    # setter methods
    def set_brand(self, brand):
        self.__brand= brand

    def set_model(self, model):
        self.__model = model
    
    def set_year(self, year):
        self.__year = year


    def __str__(self):
        return f"{self.__brand} {self.__model} ({self.__year}) - {self.__num_wheels} wheels"

v1 = Vehicle("Toyota", "Camry", 2022, 4)
v2 = Vehicle("Honda", "Civic", 2023, 4)
v3 = Vehicle("Harley", "Davidson", 2024, 2)

print(v3)
print(v2.get_brand())
v2.set_brand("Bugatti")
v2.set_model("Divo")
print(v2.get_brand(), v2.get_model())