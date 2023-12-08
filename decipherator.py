import nltk
from nltk.corpus import wordnet

class Decipherator:
    def __init__(self):
        nltk.download('wordnet')

    def decipher(self, ciphered: list, original: list, text: str) -> str:
        text_deciph = ''
        mappings = self.__create_mappings__(ciphered, original)

        word = ''
        for char in text:
            if char in mappings:
                mapped_char = mappings[char.lower()]
                word += mapped_char if char.islower() else mapped_char.upper()
            else:
                # The character isn't a letter
                # End the word and find out if it exists
                if not self.__word_exists__(word):
                    # We need to fix any broken mapping so that the words make sense
                    continue

        return text_deciph

    def __create_mappings__(ciphered: list, original: list) -> dict:
        # Zip up the ciphered letters and original letters into a dictionary
        # where the key is the ciphered letter and the value is the original
        return dict(zip(ciphered, original))

    def __word_exists__(word) -> bool:
        synsets = wordnet.synset(word)
        return len(synsets) > 0