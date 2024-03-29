#the pet class represents a pet
class Pet:
    #the __init__ method initializes the attributes
    def __init__ (self, name, animal_type, age):
        self.__name = name
        self.__animal_type = animal_type
        self.__age = age
        
    #the set_name method sets the pet's name
    def set_name(self, name):
        self.__name = name
        
    #the set_animal_type method sets the pet's type
    def set_animal_type(self, animal_type):
        self.__animal_type = animal_type
        
    #the set_age method sets the pet's age
    def set_age(self, age):
        self.__age = age
        
    #the get_name method returns the pet's name 
    def get_name(self):
        return self.__name
    
    #the get animal type method returns the pet's type
    def get_animal_type(self):
        return self.__animal_type
    
    #the get_age method returns the pet's age
    def get_age(self):
        return self.__age