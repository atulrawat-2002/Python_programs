# #############3 dynamic typing and strong typing

# def add(a, b):
#     return a + b

# print(add(4, 4))
# print(add("a", "b"))
# print(add(4, "b"))


# ########### Duck typing

def greet(obj):
    obj.say_hello()

class Person:
    def say_hello(self):
        print("Hello person")


class Robot:
    def say_hello(self):
        print("Hello robot")

greet(Person())
greet(Robot())