import string
import matplotlib.pyplot as plt

class Decipher:
    CipherText = None
    Frequency = None
    OriginalCipher = None
    FrequentMappingOrder =  [
        'E', 'T', 'A', 'O', 'I', 'N', 'S', 'H', 'R', 'D', 'L', 'C', 'U', 'M',
        'W', 'F', 'G', 'Y', 'P', 'B', 'V', 'K', 'J', 'X', 'Q', 'Z']
    
    def __init__(self, cipherText) -> None:
            self.CipherText = cipherText
            self.Frequency = self.GetFrequency(cipherText)
            self.OriginalCipher = self.CipherText

    def GetFrequency(self, cipherText):
        frequencyTable = {key: 0 for key in string.ascii_uppercase}
        for char in cipherText:
            if char.isalpha() and char.upper():
                if char in frequencyTable:
                    frequencyTable[char] += 1
                else:
                    frequencyTable[char] = 1
        return frequencyTable

    def DisplayFreqAnalysis(self):
        alphabetList = list(self.Frequency.keys())
        frequencyList = list(self.Frequency.values())
        plt.bar(alphabetList, frequencyList)
        plt.title("Frequency of Alphabets")
        plt.xlabel("Alphabets")
        plt.ylabel("Frequency")
        plt.show()
    
    def substitute(self, fromChar, toChar):
         if self.OriginalCipher:
            substituted_text = self.CipherText  # Initialize with current ciphertext
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
         self.CipherText = self.CipherText.replace(firstChar, "♛")
         self.CipherText = self.CipherText.replace(secondChar, firstChar)
         self.CipherText = self.CipherText.replace("♛", secondChar)

    
    def performDecrypt(self):
        step = 26
        if (self.Frequency != None):
            self.Frequency = dict(sorted(self.Frequency.items(),
                                         key=lambda item: item[1], reverse=True))
        orderedFreqKeys = list(self.Frequency.keys())
        for index in range(step):
            if self.OriginalCipher:
                if self.Frequency[orderedFreqKeys[index]] == 0:
                    return
                self.substitute(
                    orderedFreqKeys[index], self.FrequentMappingOrder[index])
                

cipher = """gsv jfrxp yildm ulc qfnkh levi gsrigvvm ozab wlth. Z nlmlzokszyvgrxzo hfyhgrgfgrlm xrksvi fhvh z urcvw hfyhgrgfgrlm levi gsv vmgriv nvhhztv. Gsv xrksvigvcg zokszyvg nzb yv z hsrugvw, ivevihvw, nrcvw li wvizmtvw evihrlm lu gsv kozrmgvcg zokszyvg."""
cipher = cipher.upper()

D = Decipher(cipherText=cipher)
# D.DisplayFreqAnalysis()
D.performDecrypt()
step = 0
print(D.CipherText)
                
while True:
    
    swapchar = input("Swap first letter with second letter: ").strip()
    if (swapchar.isnumeric()):
        break
    try:
        c1, c2 = swapchar.split(" ")[:2]

        D.swap(c1, c2)
        
    except:
        continue

    print("Updated\n", end=" ")
    print(D.CipherText)
    print()

    




         

