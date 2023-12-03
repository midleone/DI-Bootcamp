#EX1

# class Cat():
#     def __init__(self, cat_name, cat_age):
#         self.name = cat_name
#         self.age = cat_age
#
#
# cat1 = Cat("kiki", 7)
# cat2 = Cat("licky",3 )
# cat3 = Cat("miki", 6)
#
# cat_list = [cat1, cat2, cat3]
#
# old_cat = max(cat1.age, cat2.age, cat3.age)
#
# print(old_cat)
#
# print(f"The oldest cat is {old_cat.name}, and is {old_cat.age} years old")

#
# #EX2
# class Dog():
#     def __init__(self, name, high):
#         self.name = name
#         self.high = high
#     def  bark(self):
#         print(f'{self.name} barks! woof')
#
#     def jump(self):
#         jump_height = self.height * 2
#         print(f"{self.name} jumps {jump_height} cm high!")
#
#
# davids_dog = Dog("Rex", 50,)
# print(f"David's dog details: Name - {davids_dog.name}, Height - {davids_dog.high} cm")
#
# sarahs_dog = Dog(name="Teacup", height=20)
# print(f"Sarah's dog details: Name - {sarahs_dog.name}, Height - {sarahs_dog.height} cm")
# sarahs_dog.bark()
# sarahs_dog.jump()


# EX3
#
# class Song:
#     def __init__(self, lyrics):
#         self.lyrics = lyrics
#
#     def sing_me_a_song(self):
#         for line in self.lyrics:
#             print(line)
#
# stairway = Song(["There’s a lady who's sure", "all that glitters is gold", "and she’s buying a stairway to heaven"])
# stairway.sing_me_a_song()


#EX 4

# class zoo():
#     def __init__(self, zoo_name):
#         self.name = zoo_name
#         self.animals = []
#         def add_animal(self, new_animal):
#             if new_animal not in self.animals:
#                 self.animals.append(new_animal)
#                 print(f"{new_animal} has been added to the zoo.")
#
#         def get_animals(self):
#             print("Animals in the zoo:")
#             for animal in self.animals:
#                 print(animal)
#
#         def sell_animal(self, animal_sold):
#             if animal_sold in self.animals:
#                 self.animals.remove(animal_sold)
#                 print(f"{animal_sold} has been sold.")
#
#         def sort_animals(self):
#             sorted_animals = {}
#             for animal in sorted(self.animals):
#                 first_letter = animal[0].upper()
#                 if first_letter not in sorted_animals:
#                     sorted_animals[first_letter] = [animal]
#                 else:
#                     sorted_animals[first_letter].append(animal)
#
#             print("Sorted and grouped animals:")
#             for key, value in sorted_animals.items():
#                 print({len(value): value})

    #
    # zoo.add_animal("Ape")
    # zoo.add_animal("Bear")
    # zoo.add_animal("Cat")
    # zoo.add_animal("Baboon")
    # zoo.add_animal("Cougar")
    # zoo.add_animal("Eel")
    # zoo.add_animal("Emu")
    #
    # my_zoo.get_animals()
    #
    # my_zoo.sell_animal("Bear")
    #
    # my_zoo.get_animals()
    #
    # my_zoo.sort_animals()