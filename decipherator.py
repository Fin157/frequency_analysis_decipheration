import enchant
import helpers
import re

class Decipherator:
    __dict = enchant.Dict('en_GB')

    def decipher(ciphered: list, original: list, text: str) -> str:
        text_deciph = ''
        mappings = Decipherator.__create_mappings__(ciphered, original)

        word = ''
        for char in text:
            if char in mappings:
                mapped_char = mappings[char.lower()]
                word += mapped_char if char.islower() else mapped_char.upper()
            else:
                # The character isn't a letter
                # End the word and find out if it exists
                if not Decipherator.__word_exists__(word):
                    # We need to fix any broken mappings so that the words make sense
                    continue

        return text_deciph

    def __create_mappings__(ciphered: list, original: list) -> dict:
        # Zip up the ciphered letters and original letters into a dictionary
        # where the key is the ciphered letter and the value is the original
        return dict(zip(ciphered, original))
    
    def __fix_mappings__(mappings: dict, deciphered_text: str) -> dict:
        words = re.split(' |,|\.|!|\?', deciphered_text)
        # Initialize an empty dictionary where all 'wanted' letters
        # will be saved
        wanted_letters = {}
        correct_letters = 

        for word in words:
            if not Decipherator.__word_exists__(word):
                replacements = Decipherator.__get_replacements__(word)
                # Check there is an intersection between the wanted letters
                # and the replacements
                intersection = set(wanted_letters.keys()).intersection(replacements.keys())

    def __word_exists__(word: str) -> bool:
        variants = helpers.get_word_variants(word)
        for variant in variants:
            if Decipherator.__dict.check(variant):
                return True
        return False
    
    def __get_replacements__(word: str) -> dict:
        word_length = len(word)
        variants = helpers.get_word_variants(word)
        replacements = {}
        for variant in variants:
            suggestions = Decipherator.__dict.suggest(variant)
            for suggestion in suggestions:
                # Only proceed if the suggested word is of the same length as the original
                # and no letters are doubled (replaced to a letter already present in the word)
                if len(suggestion) == word_length and len(set(suggestion)) == len(set(word)):
                    for i in range(word_length):
                        if suggestion[i].lower() != word[i].lower():
                            replacements[word[i]] = suggestion[i]

        return replacements