import string
import tkinter as tk
from tkinter import messagebox

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

class DecipherApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Cipher Text Decryption")
        
        self.label1 = tk.Label(root, text="Enter first character:")
        self.label1.pack()
        
        self.entry1 = tk.Entry(root, width=5)
        self.entry1.pack()
        
        self.label2 = tk.Label(root, text="Enter second character:")
        self.label2.pack()
        
        self.entry2 = tk.Entry(root, width=5)
        self.entry2.pack()
        
        self.swap_button = tk.Button(root, text="Swap", command=self.perform_swap)
        self.swap_button.pack()
        
        self.result_label = tk.Label(root, text="")
        self.result_label.pack()
        
        self.cipher_text = tk.simpledialog.askstring("Input", "Enter the Cipher Text:")
        self.cipher_text = self.cipher_text.upper()
        
        self.decipher = Decipher(self.cipher_text)

    def perform_swap(self):
        c1 = self.entry1.get()
        c2 = self.entry2.get()
        if not c1 or not c2:
            messagebox.showwarning("Warning", "Please enter two characters.")
            return
        try:
            self.decipher.swap(c1, c2)
            self.result_label.config(text=self.decipher.CipherText)
        except Exception as e:
            messagebox.showerror("Error", str(e))

def main():
    root = tk.Tk()
    app = DecipherApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
