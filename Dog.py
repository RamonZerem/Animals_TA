"""
This is a class for the dog object
"""

class Dog:

    """
    The initializer function, use to initialize objects of type Dog
    :parameter self - The object itself
    :parameter breed - The dog breed
    :parameter name - The dog name
    :parameter age - The dog age
    """
    def __init__(self, name, breed, age):
        self.__name = name
        self.__breed = breed
        self.__age = age

    """
    Print the sound the dog make
    """
    def make_sound(self):
        print("Woof")

    """
    Prints the dog name, breed and age
    """
    def print_info(self):
        print("The dog " + self.__name + " of breed " + self.__breed + " is " + str(self.__age) + " years old")
