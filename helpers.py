def get_word_variants(word: str) -> list:
    return [word[0].upper() + word[1:], word[0].lower() + word[1:]]