import string


class CircularList(list):
    def __getitem__(self, index):
        return super().__getitem__(index % len(self))

    def __setitem__(self, index, value):
        super().__setitem__(index % len(self), value)


letters = string.ascii_letters
numbers = string.digits
symbols = string.punctuation
space = string.whitespace

ciphercircularlist = CircularList(letters + numbers + symbols + space)
