#EX1
# keys = ['Ten', 'Twenty', 'Thirty']
# values = [10, 20, 30]
#
# zipped_value = zip(keys, values)
# zip_list = list(zipped_value)
#
# print(zip_list)

#EX2

# family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}
# # age < 3 = "free"
# # age< 12 = 10
# # age >12 = 15
#
# for name, age in family.items():
#     if age < 3:
#         ticket_price = 0
#     elif 3 <= age <= 12:
#         ticket_price = 10
#     else:
#         ticket_price =15
#     print(f"{name}'s ticket price: ${ticket_price}")

#
# family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}
#
# for name, age in family.items():
#     if age < 3:
#         ticket_price = 0
#     elif 3 <= age <= 12:
#         ticket_price = 10
#     else:
#         ticket_price = 15
#     print(f"{name}'s ticket price: ${ticket_price}")

#EX3
# name: Zara
# creation_date: 1975
# creator_name: Amancio Ortega Gaona
# type_of_clothes: men, women, children, home
# international_competitors: Gap, H&M, Benetton
# number_stores: 7000
# major_color:
#     France: blue,
#     Spain: red,
#     US: pink, green

#EX$
# brand = {"name": "Zara", "creation_date": 1975, "type_of_clothes": ["men", "women", "children", "home"],
#          "number_stores": 2, "international_competitors": ["Gap", "H&M", "Benetton"], "major_color": {"France": 'blue',
#                                                                                                       'Spain': 'red',
#                                                                                                       'US': ['pink',
#                                                                                                              'green']}}
#
# print(f"Zara's clients are {', '.join(brand['type_of_clothes'])}.")
# brand["country_creation"] = "Spain"
# del brand["creation_date"]
#
# print("Last international competitor:", brand["international_competitors"][-1])
#
# print("Major clothes colors in the US:", brand["major_color"]["US"])
#
# print("Number of key-value pairs:", len(brand))
#
# print("Keys of the dictionary:", list(brand.keys()))
# more_on_zara = {
#     "creation_date": 1975,
#     "number_stores": 10000
# }
# brand.update(more_on_zara)
# print("Updated 'brand' dictionary:", brand)

#EX4

# users = ["Mickey","Minnie","Donald","Ariel","Pluto"]
# # disney_users_A = {}
# # for index, users in enumerate(users):
# #     disney_users_A[users] = index
# # print(disney_users_A)
# #
# #
# # # {0: "Mickey",1: "Minnie", 2: "Donald", 3: "Ariel", 4: "Pluto"}
# #
# disney_users_B ={}
# #
# for index, user in enumerate(users):
#     disney_users_B[index]= user

#     print(disney_users_B)
