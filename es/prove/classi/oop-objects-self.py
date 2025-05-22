""" A class is a collection of objects. Classes are blueprints for creating objects. A class defines a set of attributes and methods that the created objects (instances) can have.

Some points on Python class:  

Classes are created by keyword class.
Attributes are the variables that belong to a class.
Attributes are always public and can be accessed using the dot (.) operator. Example: Myclass.Myattribute
Creating a Class
Here, the class keyword indicates that we are creating a class followed by name of the class (Dog in this case). """

class Dog:                                              #class
    species = "Canine"                                  #class attribute -> shared by all class' instances
    def __init__(self, age, name, fur):                 #initialize -> init + (attributes)
        self.age = age                                  #instance attribute
        self.name = name                                #instance attribute
        self.fur = fur                                  #instance attribute

        """ Explanation:

class Dog: Defines a class named Dog.
species: A class attribute shared by all instances of the class.
__init__ method: Initializes the name and age attributes when a new object is created. """

#create an object of the dog class: An Object is an instance of a Class. It represents a specific implementation of the class and holds its own data.

dog1 = Dog(6, "Robb", "short")
print(dog1.name)
print(dog1.age)
print(dog1.fur)

dog2 = Dog(3, "JJ", "long")
print(dog2.name)
print(dog2.age)
print(dog2.fur)

if dog2.age < dog1.age:
    print("Robb is older than JJ")
