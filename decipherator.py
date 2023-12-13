import enchant
import helpers
import re
import dict_packer

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

        unknown_letters = set(mappings.keys())

        for word in words:
            # Repeat for every word in the text up until the moment
            # when we've already encountered every English letter and
            # no letter is wanted
            if len(unknown_letters) == 0 and len(wanted_letters) == 0:
                break
            # Mark all letters in this word as seen
            for letter in word:
                unknown_letters.remove(letter)
            # Proceed only if the word isn't a valid English word
            if not Decipherator.__word_exists__(word):
                # Get viable replacements from Enchant
                replacements = Decipherator.__get_replacements__(word)
                # If no replacements have been found, the word is way
                # too complicated and we ignore it
                if len(replacements) == 0:
                    continue
                # Calculate the intersection of the wanted letters and
                # the newly obtained replacements
                intersection = set(dict_packer.unpack_dict(wanted_letters)).intersection(dict_packer.unpack_dict(replacements))
                # If there is only one possible intersection
                if len(intersection) == 1:
                    # Swap letters in mappings
                    mappings[intersection[0]] = intersection[1]
                else:
                    # Add all replacements with the same letter to wanted letters
                    for letter in replacements[intersection[0]]:
                        if wanted_letters[letter] == None:
                            wanted_letters[letter] = []
                        wanted_letters[letter].append(replacements[letter])
                

        return mappings

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
                suggestions_set = set(suggestion)
                word_set = set(word)
                if len(suggestion) == word_length and len(suggestions_set) == len(word_set) and len(suggestions_set.difference(word_set)) <= 1:
                    for i in range(word_length):
                        if suggestion[i].lower() != word[i].lower():
                            replacements[word[i].lower()] = suggestion[i].lower()

        return replacements