def analyze(file_path: str):
    letters = {}

    with open(file_path, 'r') as file:
        text = file.read()
        for chunk in text:
            if chunk.isalpha():
                char = chunk.lower()
                if char in letters.keys():
                    letters[char] += 1
                else:
                    letters[char] = 1
    
    return sorted(letters, key = letters.get, reverse = True), text

def decipher(ciphered, original) -> str:
    text_deciph = ''
    mappings = create_mappings(ciphered[0], original[1])
    text_ciph = str(ciphered[1])
    for char in text_ciph:
        if char in mappings:
            mapped_char = mappings[char.lower()]
            text_deciph += mapped_char if char.islower() else mapped_char.upper()
        else:
            text_deciph += char

    return text_deciph

def create_mappings(ciphered: dict, original: dict) -> dict:
    ciphered_list = list(ciphered.keys())
    original_list = list(original.keys())
    mapping_dict = {}
    for i in range(min(len(ciphered_list), len(original_list))):
        mapping_dict[ciphered_list[i]] = original_list[i]
    return mapping_dict

def write_output(output_path: str, text_deciph: str):
    with open(output_path, 'w') as file:
        file.write(text_deciph)

def calculate(input_path: str, original_path: str, output_path: str) -> None:
    ciphered = analyze(input_path)
    original = analyze(original_path)
    output = decipher(ciphered, original)
    write_output(output_path, output)

calculate('sifrovany_text.txt', 'sherlock-holmes.txt', 'alice_in_basement.txt')