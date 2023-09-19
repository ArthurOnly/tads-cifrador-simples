from constants import cript_dict, decript_dict


class CypherHandler:
    def __init__(self, text: str, key: list):
        self.text = text
        self.key = key

    def cypher(self) -> str:
        chars_as_number = [cript_dict[char] for char in self.text]
        for i in range(len(chars_as_number)):
            chars_as_number[i] += self.key[i % len(self.key)]
            chars_as_number[i] %= len(cript_dict)
        number_as_chars = [decript_dict[number] for number in chars_as_number]
        return "".join(number_as_chars)

    def decypher(self) -> str:
        chars_as_number = [cript_dict[char] for char in self.text]
        for i in range(len(chars_as_number)):
            chars_as_number[i] -= self.key[i % len(self.key)]
            chars_as_number[i] %= len(cript_dict)
        number_as_chars = [decript_dict[number] for number in chars_as_number]
        return "".join(number_as_chars)
