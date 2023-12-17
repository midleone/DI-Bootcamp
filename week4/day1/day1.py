# 1. F-Strings
word1 = input("Enter the first word: ")
word2 = input("Enter the second word: ")
word3 = input("Enter the third word: ")
sentence = f"The words are: {word1}, {word2}, {word3}."
print(sentence)

# 2. List Exercise
string_list = ["hello", "world"]
print(string_list[1].upper())
print(string_list[0][::-1])

# 3. List of Names
names_list = ["Alice", "Bob", "Charlie", "David"]
for i in range(0, len(names_list), 2):
    print(names_list[i])

# 4. Insert Number into List
numbers_list = [1, 2, 3, 4, 5]
new_number = int(input("Enter a new number: "))
numbers_list.insert(-2, new_number)
print(numbers_list)

# 5. Dictionary Exercise
personal_info = {
    "name": "John",
    "age": 25,
    "gender": "Male",
    "favorite_food": "Pizza"
}
print(personal_info)

# 6. Blood Alcohol Level
bac = float(input("Enter your blood alcohol level: "))
if bac >= 0.5:
    print("Take a cab, you're not sober.")
else:
    print("You can drive home safely.")

# 7. Retirement Age
gender = input("Enter your gender: ")
age = int(input("Enter your age: "))
if (gender.lower() == "male" and age > 65) or (gender.lower() == "female" and age > 60):
    print("It's time to retire!")
else:
    print("Keep working!")

# 8. Loop to print numbers between 10 and 20
for num in range(10, 21):
    print(num)

# 9. Loop to print odd numbers between 1 and 20
for num in range(1, 21, 2):
    print(num)

# 10. Loop to print names from a list
names_list = ["Alice", "Bob", "Charlie", "David", "Eva"]
for name in names_list:
    print(name)

# 11. Loop to sum numbers until 0 is entered
sum_numbers = 0
while True:
    num = int(input("Enter a number (0 to stop): "))
    if num == 0:
        break
    sum_numbers += num
print("Sum of numbers:", sum_numbers)

# 12. Loop to find the longest word
longest_word = ""
while True:
    word = input("Enter a word ('done' to stop): ")
    if word == 'done':
        break
    if len(word) > len(longest_word):
        longest_word = word
print("Longest word:", longest_word)

# 13. Function to print string length
def print_length(input_string):
    print(len(input_string))

# 14. Function to calculate average
def calculate_average(num1, num2, num3):
    average = (num1 + num2 + num3) / 3
    print("Average:", average)

# 15. Function to check string length
def check_string_length(input_string, number):
    print(len(input_string) > number)

# 16. Function to copy string
def copy_string(input_string, copies=1):
    print(input_string * copies)
