
# #EX1
# class Pets():
#     def __init__(self, animals):
#         self.animals = animals
#
#     def walk(self):
#         for animal in self.animals:
#             print(animal.walk())
#
#
# class Cat():
#     is_lazy = True
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def walk(self):
#         return f'{self.name} is just walking around'
#
#
# class Bengal(Cat):
#     def sing(self, sounds):
#         return f'{sounds}'
#
#
# class Chartreux(Cat):
#     def sing(self, sounds):
#         return f'{sounds}'
#
#
# class Siamese(Cat):
#     def sing(self, sounds):
#         return f'{sounds}'
#
#
# bengal_cat = Bengal(name='BengalCat', age=3)
# chartreux_cat = Chartreux(name='ChartreuxCat', age=4)
# siamese_cat = Siamese(name='SiameseCat', age=2)
#
# all_cats = [bengal_cat, chartreux_cat, siamese_cat]
#
# sara_pets = Pets(animals=all_cats)
#
# sara_pets.walk()

#ex2
# class Dog:
#     def __init__(self, name, age, weight):
#         self.name = name
#         self.age = age
#         self.weight = weight
#
#     def bark(self):
#         return f"{self.name} is barking"
#
#     def run_speed(self):
#         return self.weight / self.age * 10
#
#     def fight(self, other_dog):
#         self_speed = self.run_speed() * self.weight
#         other_speed = other_dog.run_speed() * other_dog.weight
#
#         if self_speed > other_speed:
#             return f"{self.name} won the fight!"
#         elif self_speed < other_speed:
#             return f"{other_dog.name} won the fight!"
#         else:
#             return "It's a draw!"
#
# dog1 = Dog(name="Buddy", age=3, weight=15)
# dog2 = Dog(name="Max", age=2, weight=12)
# dog3 = Dog(name="Rocky", age=4, weight=18)
#
# print(dog1.bark())
# print(f"{dog1.name}'s running speed: {dog1.run_speed()}")
# print()
#
# print(dog2.bark())
# print(f"{dog2.name}'s running speed: {dog2.run_speed()}")
# print()
#
# print(dog3.bark())
# print(f"{dog3.name}'s running speed: {dog3.run_speed()}")
# print()
#
# fight_result = dog1.fight(dog2)
# print(fight_result)
#
# # ex4
# class Dog:
#     def __init__(self, name, age, weight):
#         self.name = name
#         self.age = age
#         self.weight = weight
#
#     def bark(self):
#         return f"{self.name} is barking"
#
#     def run_speed(self):
#         return self.weight / self.age * 10
#
#     def fight(self, other_dog):
#         self_speed = self.run_speed() * self.weight
#         other_speed = other_dog.run_speed() * other_dog.weight
#
#         if self_speed > other_speed:
#             return f"{self.name} won the fight!"
#         elif self_speed < other_speed:
#             return f"{other_dog.name} won the fight!"
#         else:
#             return "It's a draw!"
#
# #ex5

# class Family:
#     def __init__(self, last_name, members):
#         self.last_name = last_name
#         self.members = members
#
#     def born(self, **kwargs):
#         self.members.append(kwargs)
#         print(f"Congratulations! A new member, {kwargs['name']}, has been born into the {self.last_name} family.")
#
#     def is_18(self, name):
#         for member in self.members:
#             if member['name'] == name:
#                 return member['age'] >= 18
#         return False
#
#     def family_presentation(self):
#         print(f"Family {self.last_name}:")
#         for member in self.members:
#             print(f"Name: {member['name']}, Age: {member['age']}, Gender: {member['gender']}, Child: {member['is_child']}")
#
# my_family = Family(last_name="Smith", members=[
#     {'name': 'Michael', 'age': 35, 'gender': 'Male', 'is_child': False},
#     {'name': 'Sarah', 'age': 32, 'gender': 'Female', 'is_child': False}
# ])
#
# my_family.born(name='John', age=0, gender='Male', is_child=True)
#
# print(f"Is Sarah over 18? {my_family.is_18('Sarah')}")
#
# my_family.family_presentation()

