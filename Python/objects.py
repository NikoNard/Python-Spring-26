"""
demo
"""

class Employee: # class names are capitalized
    def __init__(self, fname, lname, extension, emp_num):
        self.fname = fname
        self.lname = lname
        self.extension = extension
        self.emp_num = emp_num

#setters 
    def set_fname(self, fname):
        self.fname = fname

    def set_lname(self, lname):
        self.lname = lname
    
    def set_extension(self, extension):
        self.extension = extension

    def set_emp_num(self, emp_num):
        self.emp_num = emp_num

    #getters
    def get_fname(self):
        return self.fname
    
    def get_lname(self):
        return self.lname  
    
    def get_extension(self):
        return self.extension
    
    def get_emp_num(self):
        return self.emp_num
    
    #description

    def description(self):
        print(f"{self.fname} {self.lname}\nextension: {self.extension}\nemployee number: {self.emp_num}")

    """create an employee object
    """
    empl1 = Employee("Meri", "Kasprak", "8939", 222)
    empl2 = Employee("Monty", "PyDuck", "2332", 982)

    print(empl1.get_fname(), empl1.get_lname())
    emp2.description()



"""
coffee"""

class Coffee:
    def __init__(self, coffee_type, size, milk, flavor, pumps):
        self.__coffee_type = coffee_type #double underscore makes it private
        self.__size = size
        self.__milk = milk  
        self.__flavor = flavor
        self.__pumps = pumps

    def set_coffee_type(self, coffee_type):
        self.__coffee_type = coffee_type

    def set_size(self, size):
        self.__size = size
    
    def set_milk(self, milk):
        self.__milk = milk

    def set_flavor(self, flavor):
        self.__flavor = flavor
    
    def set_pumps(self, pumps):
        self.__pumps = pumps
    
    def get_coffee_type(self):
        return self.__coffee_type

    def get_size(self):
        return self.__size
    
    def get_milk(self):
        return self.__milk
    
    def get_flavor(self):
        return self.__flavor
    
    def get_pumps(self):
        return self.__pumps
    
    def description(self):
        print(f"{self.__size} {self.__coffee_type} with {self.__milk} milk, {self.__flavor} flavor, and {self.__pumps} pumps of syrup.")
        
my_coffee = Coffee("latte", "grande", "oat", "vanilla", 3)
my_coffee.description()