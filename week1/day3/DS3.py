
#EX1
def create_index_dictionary(word):
    index_dict = {}

    for index, letter in enumerate(word):
        letter = str(letter)

        if letter not in index_dict:
            index_dict[letter] = []

        index_dict[letter].append(index)

    return index_dict

user_word = input("Enter a word: ")

result = create_index_dictionary(user_word)
print(result)

#EX2
def affordable_items(items, wallet):
    wallet_amount = int(wallet.replace("$", "").replace(",", ""))

    affordable = [item for item, price in sorted(items.items()) if int(price.replace("$", "").replace(",", "")) <= wallet_amount]

    return affordable if affordable else "Nothing"

items_purchase_1 = {
    "Water": "$1",
    "Bread": "$3",
    "TV": "$1,000",
    "Fertilizer": "$20"
}
wallet_1 = "$300"

result_1 = affordable_items(items_purchase_1, wallet_1)
print(result_1)

items_purchase_2 = {
    "Apple": "$4",
    "Honey": "$3",
    "Fan": "$14",
    "Bananas": "$4",
    "Pan": "$100",
    "Spoon": "$2"
}
wallet_2 = "$100"

result_2 = affordable_items(items_purchase_2, wallet_2)
print(result_2)

items_purchase_3 = {
    "Phone": "$999",
    "Speakers": "$300",
    "Laptop": "$5,000",
    "PC": "$1200"
}
wallet_3 = "$1"

result_3 = affordable_items(items_purchase_3, wallet_3)
print(result_3)