import string
import tkinter as tk
from tkinter import filedialog, messagebox, simpledialog
import matplotlib.pyplot as plt 

savingID = 1

class Decipher:
    CipherText = None
    Frequency = None
    OriginalCipher = None
    FrequentMappingOrder = [
        'E', 'T', 'A', 'O', 'I', 'N', 'S', 'H', 'R', 'D', 'L', 'C', 'U', 'M',
        'W', 'F', 'G', 'Y', 'P', 'B', 'V', 'K', 'J', 'X', 'Q', 'Z']

    def __init__(self, cipherText) -> None:
        # Initialize the Decipher object
        self.CipherText = cipherText
        self.Frequency = self.GetFrequency(cipherText)
        self.OriginalCipher = self.CipherText
        self.performDecrypt()
        self.mapping_history = {}  # Dictionary to store mapping history
        for original_char, mapped_char in zip(self.OriginalCipher, self.CipherText):
            if original_char.isalpha() and mapped_char.isalpha():
                self.mapping_history[original_char.upper()] = mapped_char.upper()
        self.DisplayFreqAnalysis()

    def GetFrequency(self, cipherText):
        # Calculate the frequency of each character in the cipher text
        frequencyTable = {key: 0 for key in string.ascii_uppercase}
        for char in cipherText:
            if char.isalpha() and char.upper():
                if char in frequencyTable:
                    frequencyTable[char] += 1
                else:
                    frequencyTable[char] = 1
        return frequencyTable

    def substitute(self, fromChar, toChar):
        # Substitute characters in the ciphertext
        if self.OriginalCipher:
            substituted_text = self.CipherText  # Initialize with current ciphertext
            for index, char in enumerate(self.OriginalCipher):
                if char.lower() == fromChar.lower():
                    second_char = toChar.lower()
                    substituted_text = substituted_text[:index] + \
                        second_char + substituted_text[index + 1:]

            self.CipherText = substituted_text
    
    def DisplayFreqAnalysis(self):
        # Display the frequency analysis of the cipher text
        sorted_frequency = sorted(self.Frequency.items())
        alphabetList = [item[0] for item in sorted_frequency]
        frequencyList = [item[1] for item in sorted_frequency]
        
        plt.bar(alphabetList, frequencyList)
        plt.title("Frequency of Alphabets")
        plt.xlabel("Alphabets")
        plt.ylabel("Frequency")
        plt.show()


    def swap(self, firstChar, secondChar):
        # Swap characters in the ciphertext
        firstChar = firstChar.lower()
        secondChar = secondChar.lower()
        if self.CipherText is None:
            return
        self.CipherText = self.CipherText.replace(firstChar, "♛")
        self.CipherText = self.CipherText.replace(secondChar, firstChar)
        self.CipherText = self.CipherText.replace("♛", secondChar)
        
        # Update mapping history
        for original_char, mapped_char in zip(self.OriginalCipher, self.CipherText):
            if original_char.isalpha() and mapped_char.isalpha():
                self.mapping_history[original_char.upper()] = mapped_char.upper()

    def performDecrypt(self):
        # Perform decryption based on frequency analysis
        step = 26
        if self.Frequency is not None:
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
        # Initialize the GUI application
        self.root = root
        self.root.title("Cipher Text Decryption")
        
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        padding = 100
        
        self.root.geometry(f"{screen_width-padding}x{screen_height-padding}")
        
        # Top frame for swap entry, button, and new text button
        self.top_frame = tk.Frame(root)
        self.top_frame.pack(side=tk.TOP, pady=10)

        # Label and entry for first character swap
        self.label1 = tk.Label(self.top_frame, text="First character:", font=("Arial", 20))
        self.label1.grid(row=1, column=3, padx=5, pady=2)
        
        self.entry1_var = tk.StringVar()
        self.entry1 = tk.Entry(self.top_frame, textvariable=self.entry1_var, width=1, font=("Arial", 20))  # Width set to 1 for single character entry
        self.entry1.grid(row=1, column=4, padx=5, pady=2)
        self.entry1.config(validate="key", validatecommand=(self.root.register(self.validate_entry), "%P"))
        self.entry1.bind("<Return>", lambda event: self.perform_swap())

        # Label and entry for second character swap
        self.label2 = tk.Label(self.top_frame, text="Second character:", font=("Arial", 20))
        self.label2.grid(row=1, column=5, padx=5, pady=2)
        
        self.entry2_var = tk.StringVar()
        self.entry2 = tk.Entry(self.top_frame, textvariable=self.entry2_var, width=1, font=("Arial", 20))  # Width set to 1 for single character entry
        self.entry2.grid(row=1, column=6, padx=5, pady=2)
        self.entry2.config(validate="key", validatecommand=(self.root.register(self.validate_entry), "%P"))
        self.entry2.bind("<Return>", lambda event: self.perform_swap())
        
        # Button to perform character swap
        self.swap_button = tk.Button(self.top_frame, text="Swap", command=self.perform_swap, font=("Arial", 20))
        self.swap_button.grid(row=1, column=7, padx=5, pady=2)
        
        # Button to enter new text
        self.enter_text_button = tk.Button(self.top_frame, text="Enter Text", command=self.enter_text, font=("Arial", 20))
        self.enter_text_button.grid(row=0, column=3, padx=5, pady=2)

        # Button to save to file
        self.save_button = tk.Button(self.top_frame, text="Save to File", command=self.save_to_file, font=("Arial", 20))
        self.save_button.grid(row=0, column=7, padx=5, pady=2)

        # Button for opening text file
        self.open_text_button = tk.Button(self.top_frame, text="Open Text File", command=self.open_text_file, font=("Arial", 20))
        self.open_text_button.grid(row=0, column=5, padx=5, pady=2)

        # Bottom frame for mapped text and mapping display
        self.bottom_frame = tk.Frame(root)
        self.bottom_frame.pack(side=tk.TOP, pady=10)  # Positioned at the top
        
        # Label for mapped text
        self.result_label = tk.Label(self.bottom_frame, text="", padx=20, pady=20,  background="#444444" ,wraplength=screen_width - padding, foreground="white",font=("Helvetica", 15), justify="center")
        self.result_label.pack(pady=10, padx=10)  # Added padding of 10 pixels

        # Label for mapping display
        self.mapping_label = tk.Label(self.bottom_frame, text="", font=("Arial", 14), wraplength=screen_width - 300)
        self.mapping_label.pack(pady=10)  # Added padding of 10 pixels
            

    def validate_entry(self, value):
        # Validate entry in the swap text fields
        return len(value) <= 1

    def show_cipher_text(self):
        # Prompt the user to enter the cipher text
        tk.simpledialog.Dialog.font = ("Arial", 20)
        self.cipher_text = simpledialog.askstring("Input", "Enter the Cipher Text:")
        if self.cipher_text:
            self.cipher_text = self.cipher_text.upper()

        self.decipher = Decipher(self.cipher_text)
        self.result_label.config(text=self.decipher.CipherText)
    
        self.display_mapping()

    def enter_text(self):
        # Handle event when user wants to enter new text manually
        self.result_label.config(text="")
        self.mapping_label.config(text="")
        self.show_cipher_text()

    def open_text_file(self):
        # Handle event when user wants to open a text file
        file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
        if file_path:
            try: 
                with open(file_path, 'r', encoding='utf-8') as file:
                    content = file.read().strip()
                    cipher_text = content.upper()  
                    self.decipher = Decipher(cipher_text)
                    self.result_label.config(text=self.decipher.CipherText)
                    self.display_mapping()
            except UnicodeDecodeError as e:
                print(f"UnicodeDecodeError: {e}")
                return None   

    def perform_swap(self):
        # Handle event when user wants to perform character swap
        c1 = self.entry1_var.get()
        c2 = self.entry2_var.get()
        if not c1 or not c2:
            return
        try:
            self.decipher.swap(c1, c2)
            self.result_label.config(text=self.decipher.CipherText)
            self.display_mapping()

        except Exception as e:
            messagebox.showerror("Error", str(e))

    def display_mapping(self):
        # Display the mapping history of characters
        mapping_strKey = ""
        mapping_strVal = ""
        # Sort the mapping_history dictionary items based on values
        sorted_mapping = sorted(self.decipher.mapping_history.items(), key=lambda x: x[1])
    
        for key, value in sorted_mapping:
            mapping_strKey += f"{key} "
            mapping_strVal += f"{value} " 

        self.mapping_label.config(text=(mapping_strKey + " \n" + mapping_strVal))

    def save_to_file(self):
        # Save deciphered text and mapping history to a file
        global savingID # Declare savingID as a global variable
        with open(f"output_{savingID}.txt", "w") as file:
            file.write("Cipher Text:\n")
            file.write(self.decipher.OriginalCipher + "\n\n") 
            file.write("Deciphered Text:\n")
            file.write(self.decipher.CipherText + "\n\n")
            file.write("Mapping:\n")
            sorted_mapping = sorted(self.decipher.mapping_history.items(), key=lambda x: x[1])
            for key, value in sorted_mapping:
                file.write(f"{value} : {key}\n")
        savingID += 1

def main():
    # Main function to initialize the GUI application
    root = tk.Tk()
    app = DecipherApp(root)
    
    root.mainloop()

if __name__ == "__main__":
    main()
