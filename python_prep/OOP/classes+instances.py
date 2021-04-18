# Defining a class
class Employee:
    
    # This is a constructor in Python & it's called once an object is instantiated from this class.
    def __init__(self,name,age): 
        # The self keyword is a refrence to (this) specific Object like this in other langs.
        self.name = name
        self.age  = age
    
    # These are just like getters and setters in other OOP langs.
    def get_name(self): # Instead of | employee1 = Employee() ; ## employee1.name ## we say ## employee1.get_name() ##
        return self.name

    def set_name(self,name): # Instead of | employee1 = Employee() ; ## employee1.name = adam ## we say ## employee1.set_name("adam") ##
        return self.name

    def get_age(self):
        return self.age

    def set_age(self,age):
        return self.age

# Instantiating an object from our Employee class
employee1= Employee("Adam",19)

# Setting using 2 ways / 1- Setting the attribute / 2- Using the setter method
employee1.name = "Abusamra"
employee1.set_name("Abusamra")

# Getting using 2 ways / 1- accessing the attribute / 2- using the getter method
print(employee1.get_name())
print(employee1.name)