class Employee:
    def __init__(self, name, number): 
            self.__name = name
            self.__number = number
            
    def set_name(self, name): 
            self.__name = name
            
    def set_number(self, number): 
            self.__number = number
            
    def get_name(self): 
        return self.__name
        
    def get_number(self):
        return self.__number 
        
class ShiftSupervisor(Employee):
    def __init__ (self, name, number, annual_salary, annual_bonus):
        super().__init__(name, number)
        self.__annual_salary = annual_salary
        self.__annual_bonus = annual_bonus
        
    def set_annual_salary(self, annual_salary):
        self.__annual_salary = annual_salary
        
    def set_annual_bonus(self, annual_bonus):
        self.__annual_bonus = annual_bonus
        
    def get_annual_salary(self):
        return self.__annual_salary
    
    def get_annual_bonus(self):
        return self.__annual_bonus