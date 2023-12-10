matrix_str = """7ii
Tsx
h%?
i #
sM 
$a 
#t%
^r!"""

rows = matrix_str.split("\n")

num_columns = max(len(row) for row in rows)

matrix = [[' ' for _ in range(num_columns)] for _ in range(len(rows))]

for i, row in enumerate(rows):
    for j, char in enumerate(row):
        matrix[i][j] = char

decoded_message = ''
for j in range(num_columns):
    for i in range(len(rows)):
        if matrix[i][j].isalpha():
            decoded_message += matrix[i][j]
    decoded_message += ' '

print(decoded_message)