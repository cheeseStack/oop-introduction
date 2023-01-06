example_list = ["Dave", "Rob", "Stephen"]
example_boolean = True
example_string = "hello world"
print(type(example_list))
print(type(example_boolean))
print(type(example_string))
# even a function is an instance of the function class!
def this_is_a_function(a, b):
    return a * b
print(type(this_is_a_function))

class Student():
    def __init__(self, age, name, gender, grades):
        self.age = age
        self.name = name
        self.gender = gender
        self.grades = grades
    
    def compute_average(self):
        average = sum(self.grades)/len(self.grades)
        print(f"The average for student {self.name} is {average}.")

    def __str__(self):
        # return str(self.__class__) + '/' + '\n'.join(('{} = {}'.format(item, self.__dict__[item]) for item in self.__dict__ ))
        return(str(self.__class__)) + '\n' + '\n'.join((f'{item}, {self.__dict__[item]}') for item in self.__dict__)


philani = Student(age=20, name='Philani Sithole', gender='male',grades=[64, 65])     
sarah = Student(19, 'Sarah Jones', 'female', [86,67]) 


sarah.compute_average()   

# print(philani)



# from stackoverflow to print the object props
class Element:
    def __init__(self, name, symbol, number):
        self.name = name
        self.symbol = symbol
        self.number = number

    def __str__(self):
        return  str(self.__class__) + '\n'+ '\n'.join(('{} = {}'.format(item, self.__dict__[item]) for item in self.__dict__))

elem = Element('my_name', 'some_symbol', 3)
# print(elem)