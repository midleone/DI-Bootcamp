
# #EX1
# class Currency:
#     def __init__(self, currency, amount):
#         self.currency = currency
#         self.amount = amount

#     def __str__(self):
#         return f"{self.amount} {self.currency}"

#     def __repr__(self):
#         return f"{self.amount} {self.currency}"

#     def __int__(self):
#         return self.amount

#     def __add__(self, other):
#         if isinstance(other, (int, float)):
#             return Currency(self.currency, self.amount + other)
#         elif isinstance(other, Currency):
#             if self.currency != other.currency:
#                 raise TypeError(f"Cannot add between Currency type <{self.currency}> and <{other.currency}>")
#             return Currency(self.currency, self.amount + other.amount)
#         else:
#             raise TypeError(f"Unsupported operand type: {type(other)}")

#     def __iadd__(self, other):
#         if isinstance(other, (int, float)):
#             self.amount += other
#         elif isinstance(other, Currency):
#             if self.currency != other.currency:
#                 raise TypeError(f"Cannot add between Currency type <{self.currency}> and <{other.currency}>")
#             self.amount += other.amount
#         else:
#             raise TypeError(f"Unsupported operand type: {type(other)}")
#         return self


# c1 = Currency('dollar', 5)
# c2 = Currency('dollar', 10)
# c3 = Currency('shekel', 1)
# c4 = Currency('shekel', 10)

# print(str(c1))     
# print(int(c1))    
# print(repr(c1))    
# print(c1 + 5)      
# print(c1 + c2)     
# print(c1)         
# c1 += 5
# print(c1)         
# c1 += c2
# print(c1)          



# # ex2
# # import func
# #
# # ex2 = func
# #
# # print(ex2 )


# #ex3

# # import random
# # import string
# # def generate_random_string(length=5):
# #     letters = string.ascii_letters
# #     return ''.join(random.choice(letters) for _ in range(length))
# # random_string = generate_random_string()
# # print(random_string)

# # ex4
# #
# #
# #
# # import datetime
# #
# # today_date = datetime.date.today()
# # actual_datetime = datetime.datetime.now()
# #
# #
# # print(f"Today is the {today_date}")
# # print(f"In 15 hours and 10 minutes it will be the {actual_datetime}")


# #ex 5

# # import  datetime
# #
# # today_date = datetime.date.today()
# # actual_datetime = datetime.datetime.now()
# # in_15_hours = actual_datetime + datetime.timedelta(hours=40000, minutes=50)
# #
# # print(f"Today is the {today_date.strftime("%d/%m")}")
# # print(f"In  20 days and 7 hours my birthday is it will be the {in_15_hours.strftime("%d/%m")}")

# # ex6
# from fake_module import FakeModule
# fake = FakeModule
# users = []

# def add_fake_user():
#     users_add = {"name": 'diana',
#                          "adress": 'd',
#                          "langage_code": 'ww'}
#     users.append(users_add)
# #
# for _ in range(5):
#     add_fake_user()
# for user in users:
#     print(user)





