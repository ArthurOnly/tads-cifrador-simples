from apps.cipher.constants import CircularList, ciphercircularlist


class CipherHandler:
    def __init__(self, text: str, key: list):
        self.text = text
        self.key = CircularList(key)

    def cipher(self) -> str:
        message = ""
        for i, letter in enumerate(self.text):
            letter_number = ciphercircularlist.index(letter)
            key_number = self.key[i]
            cipher_number = letter_number + key_number
            message += ciphercircularlist[cipher_number]
        return message

    def decipher(self) -> str:
        message = ""
        for i, letter in enumerate(self.text):
            letter_number = ciphercircularlist.index(letter)
            key_number = self.key[i]
            cipher_number = letter_number - key_number
            message += ciphercircularlist[cipher_number]
        return message
