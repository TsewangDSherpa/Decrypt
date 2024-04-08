import string
import matplotlib.pyplot as plt

class Decipher:
    CipherText = None
    Frequency = None
    OriginalCipher = None
    FrequentMappingOrder = [
        'E', 'T', 'A', 'O', 'I', 'N', 'S', 'H', 'R', 'D', 'L', 'C', 'U', 'M',
        'W', 'F', 'G', 'Y', 'P', 'B', 'V', 'K', 'J', 'X', 'Q', 'Z']

    def __init__(self, cipherText) -> None:
        self.CipherText = cipherText
        self.Frequency = self.GetFrequency(cipherText)
        self.OriginalCipher = self.CipherText

    def GetFrequency(self, cipherText):
        # Initialize a frequency table dictionary
        frequencyTable = {key: 0 for key in string.ascii_uppercase}
        # Count the frequency of each character in the cipher text
        for char in cipherText:
            if char.isalpha() and char.upper():
                if char in frequencyTable:
                    frequencyTable[char] += 1
                else:
                    frequencyTable[char] = 1
        return frequencyTable

    def DisplayFreqAnalysis(self):
        # Get lists of alphabet keys and corresponding frequencies
        alphabetList = list(self.Frequency.keys())
        frequencyList = list(self.Frequency.values())
        # Plot the frequency distribution
        plt.bar(alphabetList, frequencyList)
        plt.title("Frequency of Alphabets")
        plt.xlabel("Alphabets")
        plt.ylabel("Frequency")
        plt.show()

    def substitute(self, fromChar, toChar):
        if self.OriginalCipher:
            # Initialize the substituted text with the current ciphertext
            substituted_text = self.CipherText
            # Replace each occurrence of 'fromChar' with 'toChar'
            for index, char in enumerate(self.OriginalCipher):
                if char.lower() == fromChar.lower():
                    second_char = toChar.lower()
                    substituted_text = substituted_text[:index] + \
                        second_char + substituted_text[index + 1:]

            self.CipherText = substituted_text

    def swap(self, firstChar, secondChar):
        firstChar = firstChar.lower()
        secondChar = secondChar.lower()
        if self.CipherText is None:
            return
        # Replace occurrences of 'firstChar' with a temporary placeholder '♛'
        self.CipherText = self.CipherText.replace(firstChar, "♛")
        # Replace occurrences of 'secondChar' with 'firstChar'
        self.CipherText = self.CipherText.replace(secondChar, firstChar)
        # Replace occurrences of the placeholder '♛' with 'secondChar'
        self.CipherText = self.CipherText.replace("♛", secondChar)

    def performDecrypt(self):
        step = 26
        if self.Frequency is not None:
            # Sort the frequency table based on the frequency values
            self.Frequency = dict(sorted(self.Frequency.items(),
                                         key=lambda item: item[1], reverse=True))
        orderedFreqKeys = list(self.Frequency.keys())
        # Perform decryption using substitution based on frequency analysis
        for index in range(step):
            if self.OriginalCipher:
                if self.Frequency[orderedFreqKeys[index]] == 0:
                    return
                self.substitute(
                    orderedFreqKeys[index], self.FrequentMappingOrder[index])

def read_file(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.read().strip()
            content = content.upper()
        return content
    except UnicodeDecodeError as e:
        print(f"UnicodeDecodeError: {e}")
        # Handle the error as per your requirement
        return None


def main():
    # Ask user whether to read from a file or enter text manually
    choice = input("Do you want to read from a file? (Y/N): ").strip().upper()

    if choice == 'Y':
        # If user chooses to read from a file, prompt for the file name
        filename = input("Enter the file name: ").strip()
        # Read cipher text from the specified file
        cipher_text = read_file(filename)
    else:
        # If user chooses to enter text manually, prompt for the cipher text
        cipher_text = input("Please enter your Cipher Text: ").strip().upper()

    # Create a Decipher object with the provided cipher text
    D = Decipher(cipherText=cipher_text)
    # Display the frequency analysis plot of the cipher text
    D.DisplayFreqAnalysis()
    # Perform decryption based on frequency analysis
    D.performDecrypt()

    print("Deciphered Text:")
    print(D.CipherText)

    # Allow the user to interactively swap characters in the decrypted text
    while True:
        swapchar = input("(Enter any numeric value to quit): \nEnter two characters separated by spaces to be swapped: \n").strip()
        if swapchar.isnumeric():
            break
        try:
            c1, c2 = swapchar.split(" ")[:2]
            D.swap(c1, c2)
            print("Updated Cipher Text:")
            print(D.CipherText)
        except:
            print("Invalid input. Please try again.")

if __name__ == "__main__":
    main()
