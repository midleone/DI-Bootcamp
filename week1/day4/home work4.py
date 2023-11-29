# #Exercise 1
# #
# # def display_message():
# #     print("i understand nothing in phyton, lists, loops :)")
# #
# # display_message()
#
#
# #EX 2
#
# # def favorite_book(title):
# #     print(f"One of my favorite books is {title}")
# #
# # favorite_book("Harry poter")
#
# #EX 4
# #
# # import random
# # def compare_numbers(user_number):
# #     random_number = random.randint(1,100)
# #     if user_number == random_number:
# #         print("Success")
# #     else:
# #         print ('Not right')
# # user_input = int(input('Enter number 1 - 100'))
# # compare_numbers(user_input)
#
# #EX3
# # def describe_city(city, country="Unknown"):
# #     print(f"{city} is in {country}")
# # describe_city("Reykjavik", "Iceland")
# # describe_city("Paris")
#
# #EX5
# # ef make_shirt(size="large", message="I love Python"):
# #     print(f"The size of the shirt is {size} and the text is '{message}'")
# # make_shirt()
# # make_shirt(size="medium")
# # make_shirt(size="small", message="Keep coding!")
#
# # #EX6
# # def show_magicians(magicians):
# #     for magician in magicians:
# #         print(magician)
# #
# # def make_great(magicians):
# #     for i in range(len(magicians)):
# #         magicians[i] = magicians[i] + " the Great"
# #
# # magician_names = ['Harry Houdini', 'David Blaine', 'Criss Angel']
# # make_great(magician_names)
# # show_magicians(magician_names)
#
# #EX6
# def get_random_temp(season):
#     if season.lower() == 'winter':
#         lower_limit, upper_limit = -10, 16
#     elif season.lower() == 'spring':
#         lower_limit, upper_limit = 0, 23
#     elif season.lower() == 'summer':
#         lower_limit, upper_limit = 24, 40
#     elif season.lower() == 'autumn' or season.lower() == 'fall':
#         lower_limit, upper_limit = 16, 32
#     else:
#         print("Invalid season. Defaulting to all-year range.")
#         lower_limit, upper_limit = -10, 40
#
#     random_temp = round(random.uniform(lower_limit, upper_limit), 1)
#     return random_temp
#
# def main():
#     season_or_month = input("Enter the season or month number (1-12): ")
#
#     if season_or_month.isdigit():
#         month = int(season_or_month)
#         if 3 <= month <= 5:
#             season = 'spring'
#         elif 6 <= month <= 8:
#             season = 'summer'
#         elif 9 <= month <= 11:
#             season = 'autumn'
#         else:
#             season = 'winter'
#     else:
#         season = season_or_month.lower()
#
#     temperature = get_random_temp(season)
#
#     print(f"The temperature right now is {temperature} degrees Celsius.")
#     if temperature < 0:
#         print("Brrr, that’s freezing! Wear some extra layers today.")
#     elif 0 <= temperature < 16:
#         print("Quite chilly! Don’t forget your coat.")
#     elif 16 <= temperature < 23:
#         print("It's a moderate temperature. Enjoy your day!")
#     elif 24 <= temperature < 32:
#         print("Warm weather! Stay cool.")
#     else:
#         print("Hot day! Hydrate and stay cool.")
#
# # main()