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

# calculate('sifrovany_text.txt', 'sherlock-holmes.txt', 'alice_in_basement.txt')

c_letters, c_text = frequency_analysis.analyze_file('sifrovany_text.txt')
o_letters, o_text = frequency_analysis.analyze_file('sherlock-holmes.txt')
d_letters, d_text = frequency_analysis.analyze_file('alice_in_basement.txt')

letters_correct_c = ['p', 'y', 'q', 'b', 'c', 'k', 'l', 't', 'a', 'm', 'n', 'f', 'v', 'i', 'x', 'j', 'o', 'r', 'e', 'z', 'w', 'g', 'd', 'h', 'u', 's']
letters_correct_o = ['e', 't', 'a', 'o', 'i', 'h', 'n', 's', 'r', 'd', 'l', 'u', 'w', 'g', 'c', 'y', 'm', 'f', 'p', 'b', 'g', 'v', 'x', 'j', 'q', 'z']
d = Decipherator()
output = d.decipher(letters_correct_c, letters_correct_o, c_text)
write_output('test.txt', output)

print(c_letters)
print(o_letters)
print(d_letters)