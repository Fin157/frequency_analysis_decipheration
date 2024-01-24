class Decipherator:
    def decipher(self, ciphered: list, original: list, text: str) -> str:
        text_deciph = ''
        mappings = self.__create_mappings__(ciphered, original)

        hard_fix_mappings = {
            'v': 'k',
            'k': 'v',
            'm': 'w',
            'w': 'g',
            'g': 'f',
            'f': 'm',
            'x': 'q',
            'j': 'x',
            'q': 'j'
        }

        word = ''
        for char in text:
            if char in mappings:
                mapped_char = mappings[char.lower()]

                used_char = hard_fix_mappings[mapped_char] if mapped_char in hard_fix_mappings else mapped_char

                word += used_char if used_char.islower() else used_char.upper()
            else:
                text_deciph += word + char
                word = ''

        return text_deciph

    def __create_mappings__(self, ciphered: list, original: list) -> dict:
        # Zip up the ciphered letters and original letters into a dictionary
        # where the key is the ciphered letter and the value is the original
        return dict(zip(ciphered, original))