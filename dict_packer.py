from typing import List

def pack_dict(list_of_tuples: List[tuple]) -> dict:
    d = {}

    for tuple in list_of_tuples:
        key = tuple[0]
        value = tuple[1]
        if key in d:
            d[key].append(value)
        else:
            d[key] = []

    return d

def unpack_dict(dictionary: dict) -> List[tuple]:
    l = []

    for key, values in dictionary.items():
        for value in values:
            l.append((key, value))

    return l