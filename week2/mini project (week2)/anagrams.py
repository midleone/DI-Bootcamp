from anagram_checker import AnagramChecker

def show_menu():
    print("\nMenu:")
    print("1. Input a word")
    print("2. Exit")

def get_user_input():
    return input("Enter your choice: ")

def validate_word(word):
    if len(word.split()) > 1:
        print("Error: Only a single word is allowed.")
        return False
    elif not word.isalpha():
        print("Error: Only alphabetic characters are allowed.")
        return False
    else:
        return True

def main():
    anagram_checker = AnagramChecker("sowpods.txt")

    while True:
        show_menu()
        choice = get_user_input()

        if choice == '1':
            user_input = input("Enter a word: ").strip()
            user_input = user_input.lower()

            if validate_word(user_input):
                anagrams = anagram_checker.get_anagrams(user_input)
                print(f"\nWord: {user_input}")
                print(f"Anagrams: {', '.join(anagrams)}")
            else:
                continue

        elif choice == '2':
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please choose again.")

if __name__ == "__main__":
    main()