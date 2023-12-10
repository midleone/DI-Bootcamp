 #Daily chalange
#EX2
# user_word = "ppoeemm"
# output =user_word[0]
# #output - P
# for i, char in enumerate(user_word):
#     if user_word[i] != user_word[i+1]:
#         output += char
#
# print(output)
#
#EX1
def generate_multiples(number, length):
    multiples_list = [number * i for i in range(1, length + 1)]
    return multiples_list

try:
    user_number = int(input("Enter a number: "))
    user_length = int(input("Enter the length: "))

    result = generate_multiples(user_number, user_length)
    print(result)

except ValueError:
    print("Please enter valid integer values for number and length.")