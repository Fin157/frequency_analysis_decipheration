from unidecode import unidecode

def analyze_file(file_path: str) -> (list, str):
    # All letter counts will be saved into this dictionary
    letters = {}

    # Open the file for reading
    with open(file_path, 'r', encoding = 'utf-8') as file:
        # Load all text from the file into a variable
        text = unidecode(file.read())
        for char in text:
            # Proced only if the character is a letter
            if char.isalpha():
                # Make sure we consider capital and non-capital letters the same letter
                char = char.lower()
                # If the letter is already present in the dictionary, increment the value at that key
                if char in letters.keys():
                    letters[char] += 1
                # Otherwise set the value to 1 which also adds the key to the dictionary
                else:
                    letters[char] = 1
    
    # Return the sorted dictionary and the text from the file
    return sorted(letters, key = letters.get, reverse = True), text