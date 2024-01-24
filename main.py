import frequency_analysis
from decipherator import Decipherator

def write_output(output_path: str, text_deciph: str):
    with open(output_path, 'w', encoding = 'utf-8') as file:
        file.write(text_deciph)

def calculate(input_path: str, original_path: str, output_path: str) -> None:
    ciphered, text = frequency_analysis.analyze_file(input_path)
    original, _ = frequency_analysis.analyze_file(original_path)
    decipherator = Decipherator()
    output = decipherator.decipher(ciphered, original, text)
    write_output(output_path, output)

calculate('sifrovany_text.txt', 'sherlock-holmes.txt', 'alice_in_basement.txt')