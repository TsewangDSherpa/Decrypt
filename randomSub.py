import random
import string
import matplotlib.pyplot as plt
import textwrap
random.seed(1)


def generate_random_mapping():
    alphabet = list(string.ascii_uppercase)
    shuffled_alphabet = alphabet[:]  # Create a copy of alphabet
    random.shuffle(shuffled_alphabet)

    mapping = {}
    for original, cipher in zip(alphabet, shuffled_alphabet):
        mapping[original] = cipher

    return mapping


def encrypt_with_random_substitution(plaintext, mapping):
    ciphertext = ""

    for char in plaintext:
        if char in mapping:
            ciphertext += mapping[char]
            # print(mapping[char] + " " + char)
        else:
            ciphertext += char
    return ciphertext


def encrypt_text_with_random_substitution(plaintext):
    mapping = generate_random_mapping()
    return encrypt_with_random_substitution(plaintext, mapping)


class Decipher:
    cipherText = None
    MainCipherText = None
    frequency = None
    mappingOrder = ['E', 'T', 'A', 'I', 'N', 'O', 'S', 'H', 'R', 'D', 'L',
                    'U', 'C', 'M', 'F', 'W', 'Y', 'G', 'P', 'B', 'V', 'K', 'Q', 'J', 'X', 'Z']

    def __init__(self, inputText) -> None:
        self.frequency = self.GetFrequency(inputText)
        self.cipherText = textwrap.fill(inputText, width=117)
        self.MainCipherText = textwrap.fill(inputText, width=117)

    def substitute(self, firstChar: chr, secondChar: chr) -> None:
        if firstChar.lower() != secondChar.lower():
            if not self.validateSwap(secondChar):
                return
        if self.MainCipherText:
            substituted_text = self.cipherText  # Initialize with current ciphertext
            for index, char in enumerate(self.MainCipherText):
                if char == firstChar or char.lower() == firstChar.lower():
                    if firstChar == secondChar:
                        second_char = secondChar.upper()
                    else:
                        second_char = secondChar.lower()
                    substituted_text = substituted_text[:index] + \
                        second_char + substituted_text[index + 1:]

            self.cipherText = textwrap.fill(substituted_text, width=117)

    def performDecrypt(self, step=26):
        if (self.frequency != None):
            self.frequency = dict(sorted(self.frequency.items(),
                                         key=lambda item: item[1], reverse=True))

        orderedFreqKeys = list(self.frequency.keys())
        for index in range(step):
            if self.cipherText:
                if self.frequency[orderedFreqKeys[index]] == 0:
                    return
                self.substitute(
                    orderedFreqKeys[index], self.mappingOrder[index])
                # print(f"{orderedFreqKeys[index]}\
                #           --> {self.mappingOrder[index]}")

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

    def validateSwap(self, toLetter):
        for index, char in enumerate(self.cipherText):

            if char == toLetter.lower():
                print("index " + str(index) + " change " +
                      self.MainCipherText[index] + " first")
                print("Can't swap " + toLetter)
                return False
        return True


if __name__ == "__main__":
    plaintext = """His book titled “Omnivore’s Dilemma: A Natural History of Four Meals” discusses several aspects of nature and focuses specifically on grass and what it is for animals and different people. Without grass life would have many problems, as both animals and humans very much need on it to live full lives.

Expectations that society has is centered on food and that it is provided in abundance for stores and markets but how it gets there, no one wonders. The author starts out by making a very specific and acute observation that most people see grass as a unit, one entity that is a part and mostly, an insignificant piece of the environment comparing to the rest of nature’s objects.

Walking on it every day, an individual never really stops and thinks what grass consists of and how its life processes are carried out. Michael Pollan mentions that the majority of people do not see grass the same way a cow sees it. As cows eat it every day, they have become specialists in the kinds of grass there are and what specific ones should not be eaten. A farmer also sees grass as a part of his life because he needs it for his cows to survive and his farm to prosper.

The author goes on to talk about his visit to the farm and how he was explained about the different types and strands of grass. People who are closely involved with farming are also knowledgeable about grass and how to properly grow it (Pollan, 2007). The expectations that people have towards grass and what farmers think, are very different. People want to see grass on their lawn to look pretty and to cover the mud. Farmers expect grass to be well grown and full of vitamins for their live stock.

Grass is a very needed and essential part of the farm and the chain of production because so many species of animals depend on it. Grass’ growth and the cows’ eating habits have many “rules and laws” that surround this food type. “The law of the second bite” is an important one to keep in mind, as the cows should not be permitted to completely eat the grass down to the root (Pollan, 2007). In case this does happen, and it mostly does, the grass becomes weakened and stops growing.

After the cows have taken the first bite, grass should be left alone, as it will have a chance to replenish itself and continue healthy growth. The opposite it true because if the grass is left to grow out more than it is supposed to, the area becomes too “bushy” and cannot be used for cows. A farmer, who is taking care of his animals and their food, will rotate to make sure the animals are moved to a new patch of grass and this makes for best results for grass, animals and people (Pollan, 2007)."""
    ciphertext = encrypt_text_with_random_substitution(
        plaintext=plaintext.upper())
print("\n")

# print(ciphertext)
D = Decipher(ciphertext)
# D.DisplayFreqAnalysis()
D.performDecrypt(26)
# print("Original\n", end=" ")
# print(D.MainCipherText)
# print()
file_path = "output.txt"

# Write the text to the file
with open(file_path, "w") as file:
    file.write(D.MainCipherText + "\n" + str(D.frequency))

print("Updated\n", end=" ")
print(D.cipherText)
print()
print(D.frequency)
while True:
    swapchar = input("Swap first letter with second letter: ").strip()
    if (swapchar.isnumeric()):
        break
    try:
        c1, c2 = swapchar.split(" ")[:2]

        D.substitute(c1, c2)
    except:
        continue

    print("Updated\n", end=" ")
    print(D.cipherText)
    print()
