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
        
class ProductionWorker(Employee):
    def __init__(self, name, number, shift, hourly_rate):
        super().__init__(name, number)
        self.__shift = shift
        self.__hourly_rate = hourly_rate
        
    def set_shift(self, shift):
        self.__shift = shift
       
    def set_hourly_rate(self, hourly_rate): 
        self.__hourly_rate = hourly_rate
        
    def get_shift(self):
        return self.__shift
    
    def get_hourly_rate(self):
        return self.__hourly_rate