#EX1
# my_fav_numbers= set()
# my_fav_numbers={13,2,5}
# my_fav_numbers.add(11)
# my_fav_numbers.add(4)
#
# # my_fav_numbers.discard(4)
# my_fav_numbers.remove(4)
#
# print(my_fav_numbers)
#
# friend_fav_numbers = set()
# friend_fav_numbers = {7,9,0,5}
#
# our_fav_numbers= set.union(my_fav_numbers,friend_fav_numbers)
# print(our_fav_numbers)


# EX2
# no, we cant

#EX3
# basket = ["Banana", "Apples", "Oranges", "Blueberries"]
# basket.append('kivi')
# basket.append('Apples')
# basket.remove('Banana')
# basket.remove('Blueberries')
# apple_count = basket.count("Apples")
# print(apple_count)
# basket.clear()
#
# print(basket)


# #EX4
# my_list = [x / 2 for x in range(3,11)]
# print(my_list)

#EX5

#
# for number in range(1, 21):
#     print(number)

#
# for number in range(1, 21):
#     if number % 2 == 0:
#         print(number)


# #EX6
#
# my_name = "diana"
# while True:
#     user_name = input("what is your name ?")
#     if user_name == my_name:
#         break


#EX7
# user_fruit =input("Enter your favorite fruits separated by a space: ")
# favorite_fruits = user_fruit.split()
# user_input_fruit = input("Enter a fruit name: ")
# if user_input_fruit in favorite_fruits:
#     print("You chose one of your favorite fruits! Enjoy!")
# else:
#     print("You chose a new fruit. I hope you enjoy.")


#EX8
# toppings =[]
# total_price = 10
#
# while True:
#     topping = input("Enter a pizza topping (type 'quit' to finish): ")
#
#     if topping.lower() == 'quit':
#         break
#
# toppings.append(topping)
# print(f"Adding {topping} to your pizza.")
# total_price += 2.5
# print("\nYour pizza toppings:")
# for topping in toppings:
#     print("- " + topping)
#
# print("\nTotal price: $", total_price)

#EX9
# family_size = int(input("Enter the number of people in the family: "))
# total_cost = 0
#
# for _ in range(family_size):
#     age = int(input("Enter the age of a person: "))
#
#     if age < 3:
#
#         print("The ticket is free for this person.")
#     elif 3 <= age <= 12:
#
#         total_cost += 10
#         print("The ticket costs $10 for this person.")
#     else:
#
#         total_cost += 15
#         print("The ticket costs $15 for this person.")
#
# print(f"\nThe total cost for the family's tickets is ${total_cost}")

#EX10

sandwich_orders = ["Tuna sandwich", "Pastrami sandwich", "Avocado sandwich", "Pastrami sandwich", "Egg sandwich", "Chicken sandwich", "Pastrami sandwich"]
finished_sandwiches= []
while "Pastrami sandwich" in sandwich_orders:
    sandwich_orders.remove("Pastrami sandwich")
finished_sandwiches = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    finished_sandwiches.append(current_sandwich)
    print(f"Making {current_sandwich}.")

print("\nList of finished sandwiches:")
for sandwich in finished_sandwiches:
    print(sandwich))