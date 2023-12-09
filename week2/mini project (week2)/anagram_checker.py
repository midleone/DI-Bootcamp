class AnagramChecker:
    def __init__(self, sowpods_f):
        self.sowpods = self.load_word_list(sowpods_f)

    def load_word_list(self, sowpods_f):
        try:
            with open(sowpods_f, 'r') as file:
                return set(word.strip().lower() for word in file)
        except FileNotFoundError:
            print(f"Error: Word list file '{sowpods_f}' not found.")
            return set()

    def is_valid_word(self, word):
        return word.lower() in self.sowpods

    def is_anagram(self, word1, word2):
        return sorted(word1.lower()) == sorted(word2.lower())

    def get_anagrams(self, word):
        return [w for w in self.sowpods if self.is_anagram(word, w) and word.lower() != w]






# if __name__ == "__main__":
#     anagram_checker = AnagramChecker("sowpods.txt")
#
#     user_input = input("Enter a word: ")
#
#     if anagram_checker.is_valid_word(user_input):
#         anagrams = anagram_checker.get_anagrams(user_input)
#         print(f"Anagrams for '{user_input}': {anagrams}")
#     else:
#         print(f"'{user_input}' is not a valid word.")
#