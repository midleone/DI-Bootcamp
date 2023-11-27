#Exercises
#EX1
# print('Hello')
# print('Hello')
# print('Hello')
# print('Hello')

#EX2
#print((99 ** 3)*8)

#EX3
# print(f"5 < 3: {5 < 3}")
# print(f'3 == "3 ": {3 == "3"}')
# print(f'"Hello" == "hello": {"Hello" == "hello"}')
# >>> 5 < 3  FALSE
# >>> 3 == 3  TRUE
# >>> 3 == "3"  FALSE
# >>> "3" > 3 FALSE
# >>> "Hello" == "hello" FALSE

# #EX4
# computer_brand= "macPro"
# print("I have a {}".format(computer_brand))
# print(f"I have a {computer_brand} ")
#

#EX5
#
# name= "Diana"
# age= "24"
# shoe_size= "37"
# info= f'My name is {name} ,my age is {age},my shoe size is {shoe_size}'
# print(f'{info}')

#EX6
# a= 5
# b= 2
# if a > b:
#     print('Hello World')
# elif a < b:
#     print('Bye')

#EX7
# user_number = int(input("Enter a number: "))
# if user_number % 2 == 0:
#     print(f"{user_number} is an even number.")
# else:
#     print(f"{user_number} is an odd number.")

# #EX8
# user_name= input('give me your name:')
# my_name= "Diana"
# if user_name == my_name:
#     print('It is the same')
# else:
#     print("Why don't scientists trust atoms? Because they make up everything!")

# #EX9
# height_inches = float(input("What is your height in inches? "))
# height_cm = height_inches * 2.54
# if height_cm > 145:
#     print("You are tall enough to ride")
# else:
#     print("Sorry, you need to grow some more to ride")


#Exercises XP Gold
#EX1
# print('Hello world')
# print('Hello world')
# print('Hello world')
# print('Hello world')
# print('I love python')
# print('I love python')
# print('I love python')
# print('I love python')

# #EX2
# user_month= int(input ('input a month from 1 to 12:'))
# if 3 <= user_month <= 5:
#     print("Spring")
# elif 6 <= user_month <= 8:
#     print("Summer")
# elif 9 <= user_month <= 11:
#     print("Autumn")
# elif user_month == 12 or 1 <= user_month <= 2:
#     print("WINTER")

#Daily Challenge: Build Up A String

import random

user_string = input("Enter a string (10 characters long): ")
if len(user_string) < 10:
    print("String not long enough.")
elif len(user_string) > 10:
    print("String too long.")
else:
    print("Perfect string!")

print("First character:", user_string[0])
print("Last character:", user_string[-1])
print("Constructing the string character by character:")
for char in user_string:
        print(char)

shuffled_string = list(user_string)
random.shuffle(shuffled_string)
shuffled_string = ''.join(shuffled_string)
print("Jumbled string:", shuffled_string)