import random
import string
import matplotlib.pyplot as plt
import numpy as np


def generate_random_mapping():  # For Test Purpose
    alphabet = string.ascii_uppercase + string.ascii_lowercase
    shuffled_alphabet = list(alphabet)
    random.seed(0)  # For testing, kept the seed of 0
    random.shuffle(shuffled_alphabet)

    mapping = {}
    for char in string.ascii_uppercase:
        cipher_char = shuffled_alphabet.pop()
        mapping[char] = cipher_char.upper()
        mapping[char.lower()] = cipher_char.lower()

    return mapping


def encrypt_with_random_substitution(plaintext, mapping):
    ciphertext = ""
    for char in plaintext:
        if char in mapping:
            ciphertext += mapping[char]
        else:
            ciphertext += char
    # print(mapping)
    return ciphertext


def encrypt_text_with_random_substitution(plaintext):
    mapping = generate_random_mapping()
    return encrypt_with_random_substitution(plaintext, mapping)


# Steps: Now do frequency analysis
# plaintext = "A monoalphabetical substitution cipher uses a fixed substitution over the entire message. The ciphertext alphabet may be a shifted, reversed, mixed or deranged version of the plaintext alphabet."
# ciphertext = encrypt_text_with_random_substitution(plaintext)
# print("Plaintext:", plaintext)
# print("Ciphertext:", ciphertext)


class Decipher:
    cipherText = None
    frequency = None
    mappingOrder = ['E', 'T', 'A', 'I', 'N', 'O', 'S', 'H', 'R', 'D', 'L',
                    'U', 'C', 'M', 'F', 'W', 'Y', 'G', 'P', 'B', 'V', 'K', 'Q', 'J', 'X', 'Z']

    def __init__(self, inputText) -> None:
        self.frequency = self.GetFrequency(inputText)
        self.cipherText = inputText

    def substitute(self, firstChar: chr, secondChar: chr) -> None:
        # use + as temp value
        if self.cipherText:
            self.cipherText = self.cipherText.replace(firstChar.lower(), '+')
            self.cipherText = self.cipherText.replace(
                secondChar.lower(), firstChar.lower())
            self.cipherText = self.cipherText.replace('+', secondChar.lower())
            self.cipherText = self.cipherText.replace(firstChar.upper(), '+')
            self.cipherText = self.cipherText.replace(
                secondChar.upper(), firstChar.upper())
            self.cipherText = self.cipherText.replace('+', secondChar.upper())

    def firstDecrypt(self):
        if (self.frequency != None):
            self.frequency = dict(sorted(self.frequency.items(),
                                         key=lambda item: item[1], reverse=True))
        for index in range(len(self.frequency.keys())):
            if (self.cipherText):
                # eat ~at ~et  aet
                self.cipherText = self.cipherText.replace(
                    self.mappingOrder[index], "~")
                self.cipherText = self.cipherText.replace(list(self.frequency.keys())[index].lower(), self.mappingOrder[index]
                                                          )
                self.cipherText = self.cipherText.replace("~",
                                                          list(self.frequency.keys())[index].lower())

                print("replacing " + list(self.frequency.keys())
                      [index] + " with " + self.mappingOrder[index])

    def GetFrequency(self, input_text):
        frequencyTable = {key: 0 for key in string.ascii_uppercase}
        for char in input_text:
            if char.isalpha():
                if char.upper() in frequencyTable:
                    frequencyTable[char.upper()] += 1
                else:
                    frequencyTable[char.upper()] = 1
        return frequencyTable

    def DisplayFreqAnalysis(self):
        alphabetList = list(self.frequency.keys())
        frequencyList = list(self.frequency.values())
        plt.bar(alphabetList, frequencyList)
        plt.title("Frequency of Alphabets")
        plt.xlabel("Alphabets")
        plt.ylabel("Frequency")
        plt.show()


if __name__ == "__main__":
    # plaintext = "Dogs are often regarded as man's best friend, and for good reason. Throughout history, these loyal companions have been by our sides, offering unwavering loyalty, companionship, and love. Their innate ability to understand human emotions and respond with empathy makes them invaluable members of our families. Whether it's a playful game of fetch, a comforting snuggle on the couch, or a reassuring presence during difficult times, dogs have an uncanny knack for brightening our days and easing our burdens. Their unwavering devotion knows no bounds, as they eagerly anticipate our return home and greet us with boundless enthusiasm each time. Beyond mere companionship, dogs also serve as protectors, guardians, and service animals, selflessly devoting themselves to our well-being. From providing emotional support to assisting those with disabilities, dogs continually demonstrate their incredible capacity for understanding and compassion. In essence, the bond between humans and dogs transcends mere friendship, evolving into a profound and enduring partnership that enriches our lives in countless ways."
    # ciphertext = encrypt_text_with_random_substitution(plaintext=plaintext)
    ciphertext = "AAoo bot aaoo"
    print("\n")
    D = Decipher(ciphertext)

    D.substitute('a', 'o')
    D.substitute('O', 'a')
    # D.substitute('a', 'c')

    print(D.cipherText)
    # D.DisplayFreqAnalysis()
    # D.firstDecrypt()
    # D.DisplayFreqAnalysis()

    # print(D.cipherText)
