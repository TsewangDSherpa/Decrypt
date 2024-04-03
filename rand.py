class Decrypt:
    cipherText = None
    MainCipherText = None
    frequency = None
    mappingOrder = ['E', 'T', 'A', 'I', 'N', 'O', 'S', 'H', 'R', 'D', 'L',
                    'U', 'C', 'M', 'F', 'W', 'Y', 'G', 'P', 'B', 'V', 'K', 'Q', 'J', 'X', 'Z']

    def __init__(self, inputText) -> None:
        self.frequency = self.GetFrequency(inputText)
        self.cipherText = inputText
        self.MainCipherText = inputText
