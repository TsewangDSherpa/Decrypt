import string
import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog

class Decipher:
    CipherText = None
    Frequency = None
    OriginalCipher = None
    FrequentMappingOrder =  [
        'E', 'T', 'A', 'O', 'I', 'N', 'S', 'H', 'R', 'D', 'L', 'C', 'U', 'M',
        'W', 'F', 'G', 'Y', 'P', 'B', 'V', 'K', 'J', 'X', 'Q', 'Z']
    CurrentMapping = None
    tempMappingDic = None
    def __init__(self, cipherText) -> None:
        self.CipherText = cipherText
        self.Frequency = self.GetFrequency(cipherText)
        self.OriginalCipher = self.CipherText
        self.performDecrypt()
        if self.tempMapping:
            self.CurrentMapping = self.tempMappingDic 
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

class DecipherApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Cipher Text Decryption")
        
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        padding = 100
        
        self.root.geometry(f"{screen_width-padding}x{screen_height-padding}")
        
        # Top frame for swap entry, button, and new text button
        self.top_frame = tk.Frame(root)
        self.top_frame.pack(side=tk.TOP, pady=10)

        self.label1 = tk.Label(self.top_frame, text="Enter first character:")
        self.label1.grid(row=0, column=0, padx=5)
        
        self.entry1_var = tk.StringVar()
        self.entry1 = tk.Entry(self.top_frame, textvariable=self.entry1_var, width=1)  # Width set to 1 for single character entry
        self.entry1.grid(row=0, column=1, padx=5)
        self.entry1.config(validate="key", validatecommand=(self.root.register(self.validate_entry), "%P"))
        self.entry1.bind("<Return>", lambda event: self.perform_swap())

        self.label2 = tk.Label(self.top_frame, text="Enter second character:")
        self.label2.grid(row=0, column=2, padx=5)
        
        self.entry2_var = tk.StringVar()
        self.entry2 = tk.Entry(self.top_frame, textvariable=self.entry2_var, width=1)  # Width set to 1 for single character entry
        self.entry2.grid(row=0, column=3, padx=5)
        self.entry2.config(validate="key", validatecommand=(self.root.register(self.validate_entry), "%P"))
        self.entry2.bind("<Return>", lambda event: self.perform_swap())
        
        self.swap_button = tk.Button(self.top_frame, text="Swap", command=self.perform_swap)
        self.swap_button.grid(row=0, column=4, padx=5)
        
        # Button to enter new text
        self.new_text_button = tk.Button(self.top_frame, text="Decipher Again", command=self.enter_new_text)
        self.new_text_button.grid(row=0, column=5, padx=5)

        # Bottom frame for mapped text
        self.bottom_frame = tk.Frame(root)
        self.bottom_frame.pack(side=tk.TOP, pady=10)  # Positioned at the top
        
        # Label for mapped text
        self.result_label = tk.Label(self.bottom_frame, text="", wraplength=screen_width - padding)
        self.result_label.pack(pady=30)  # Added padding of 30 pixels
        self.cipher_text = simpledialog.askstring("Input", "Enter the Cipher Text:")
        self.cipher_text = self.cipher_text.upper()
        # Initialize Decipher object with entered text
        self.decipher = Decipher(self.cipher_text)
        self.result_label.config(text=self.decipher.CipherText)
        

    def validate_entry(self, value):
        return len(value) <= 1

    def show_cipher_text(self):
        self.cipher_text = simpledialog.askstring("Input", "Enter the Cipher Text:")
        self.cipher_text = self.cipher_text.upper()
        self.decipher = Decipher(self.cipher_text)
        self.perform_swap()        
        self.result_label.config(text=self.decipher.CipherText)

    def perform_swap(self):
        c1 = self.entry1_var.get()
        c2 = self.entry2_var.get()
        if not c1 or not c2:
            return
        try:
            self.decipher.swap(c1, c2)
            self.result_label.config(text=self.decipher.CipherText)
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def enter_new_text(self):
        self.result_label.config(text="")
        self.show_cipher_text()

def main():
    root = tk.Tk()
    app = DecipherApp(root)
    
    root.mainloop()

if __name__ == "__main__":
    main()

