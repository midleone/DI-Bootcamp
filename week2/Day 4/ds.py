class Text:
    def __init__(self, text):
        self.text = text

    def word_frequency(self, word):
        words = self.text.split()
        word_count = words.count(word)
        return f"The word '{word}' appears {word_count} times in the text."

    def most_common_word(self):
        words = self.text.split()
        word_counts = {word: words.count(word) for word in set(words)}
        most_common = max(word_counts, key=word_counts.get)
        return f"The most common word is '{most_common}'."

    def unique_words(self):
        words = self.text.split()
        unique_words = set(words)
        return f"List of unique words: {', '.join(unique_words)}."

    @classmethod
    def from_file(cls, filename):  # Fix the parameter here
        with open(filename, 'r', encoding='utf-8') as file:
            text = file.read()
        return cls(text)


file_text_analyzer = Text.from_file('the_stranger.txt')
word_to_check = ("smile")
print(file_text_analyzer.word_frequency(word_to_check))
