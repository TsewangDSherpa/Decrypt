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
         print("substituting")
         if not self.validateSubstitution(toChar):
                print("not validedate")
                return
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
         self.CipherText = self.CipherText.replace(firstChar.upper(), "♛")
         self.CipherText = self.CipherText.replace(secondChar.upper(), firstChar)
         self.CipherText = self.CipherText.replace("♛", secondChar)

    def swap2(self, firstChar, secondChar):
         print("swapping")
         firstChar = firstChar.lower()
         secondChar = secondChar.lower()
         if self.CipherText is None:
              return
         self.CipherText = self.CipherText.replace(firstChar, "♛")
         self.CipherText = self.CipherText.replace(secondChar, firstChar)
         self.CipherText = self.CipherText.replace("♛", secondChar)
    
    def validateSubstitution(self, toLetter):
        for index, char in enumerate(self.CipherText):
            if char == toLetter.lower():
                print("Can't swap " + toLetter, end=", ")
                print( char + " is already mapped to " +
                      self.OriginalCipher[index])
                
                return False
        return True
    
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
                

cipher = """ZTU YHHJ OTORWK “HQATDHMW’U KTRWQQX: X AXOPMXR ZTUOHMS HB BHPM QWXRU” KTULPUUWU UWDWMXR XUVWLOU HB AXOPMW XAK BHLPUWU
UVWLTBTLXRRS HA FMXUU XAK IZXO TO TU BHM XATQXRU XAK KTBBWMWAO VWHVRW. ITOZHPO FMXUU RTBW IHPRK ZXDW QXAS VMHYRWQU,
XU YHOZ XATQXRU XAK ZPQXAU DWMS QPLZ AWWK HA TO OH RTDW BPRR RTDWU.  WCVWLOXOTHAU OZXO UHLTWOS ZXU TU LWAOWMWK HA
BHHK XAK OZXO TO TU VMHDTKWK TA XYPAKXALW BHM UOHMWU XAK QXMJWOU YPO ZHI TO FWOU OZWMW, AH HAW IHAKWMU. OZW XPOZHM
UOXMOU HPO YS QXJTAF X DWMS UVWLTBTL XAK XLPOW HYUWMDXOTHA OZXO QHUO VWHVRW UWW FMXUU XU X PATO, HAW WAOTOS OZXO TU X
VXMO XAK QHUORS, XA TAUTFATBTLXAO VTWLW HB OZW WADTMHAQWAO LHQVXMTAF OH OZW MWUO HB AXOPMW’U HYNWLOU.  IXRJTAF HA TO
WDWMS KXS, XA TAKTDTKPXR AWDWM MWXRRS UOHVU XAK OZTAJU IZXO FMXUU LHAUTUOU HB XAK ZHI TOU RTBW VMHLWUUWU XMW LXMMTWK
HPO. QTLZXWR VHRRXA QWAOTHAU OZXO OZW QXNHMTOS HB VWHVRW KH AHO UWW FMXUU OZW UXQW IXS X LHI UWWU TO. XU LHIU WXO TO
WDWMS KXS, OZWS ZXDW YWLHQW UVWLTXRTUOU TA OZW JTAKU HB FMXUU OZWMW XMW XAK IZXO UVWLTBTL HAWU UZHPRK AHO YW WXOWA. X
BXMQWM XRUH UWWU FMXUU XU X VXMO HB ZTU RTBW YWLXPUW ZW AWWKU TO BHM ZTU LHIU OH UPMDTDW XAK ZTU BXMQ OH VMHUVWM.
OZW XPOZHM FHWU HA OH OXRJ XYHPO ZTU DTUTO OH OZW BXMQ XAK ZHI ZW IXU WCVRXTAWK XYHPO OZW KTBBWMWAO OSVWU XAK UOMXAKU
HB FMXUU. VWHVRW IZH XMW LRHUWRS TADHRDWK ITOZ BXMQTAF XMW XRUH JAHIRWKFWXYRW XYHPO FMXUU XAK ZHI OH VMHVWMRS FMHI TO
(VHRRXA, 2007). OZW WCVWLOXOTHAU OZXO VWHVRW ZXDW OHIXMKU FMXUU XAK IZXO BXMQWMU OZTAJ, XMW DWMS KTBBWMWAO. VWHVRW
IXAO OH UWW FMXUU HA OZWTM RXIA OH RHHJ VMWOOS XAK OH LHDWM OZW QPK. BXMQWMU WCVWLO FMXUU OH YW IWRR FMHIA XAK BPRR
HB DTOXQTAU BHM OZWTM RTDW UOHLJ.  FMXUU TU X DWMS AWWKWK XAK WUUWAOTXR VXMO HB OZW BXMQ XAK OZW LZXTA HB VMHKPLOTHA
YWLXPUW UH QXAS UVWLTWU HB XATQXRU KWVWAK HA TO. FMXUU’ FMHIOZ XAK OZW LHIU’ WXOTAF ZXYTOU ZXDW QXAS “MPRWU XAK RXIU”
OZXO UPMMHPAK OZTU BHHK OSVW. “OZW RXI HB OZW UWLHAK YTOW” TU XA TQVHMOXAO HAW OH JWWV TA QTAK, XU OZW LHIU UZHPRK
AHO YW VWMQTOOWK OH LHQVRWOWRS WXO OZW FMXUU KHIA OH OZW MHHO (VHRRXA, 2007). TA LXUW OZTU KHWU ZXVVWA, XAK TO QHUORS
KHWU, OZW FMXUU YWLHQWU IWXJWAWK XAK UOHVU FMHITAF.  XBOWM OZW LHIU ZXDW OXJWA OZW BTMUO YTOW, FMXUU UZHPRK YW RWBO
XRHAW, XU TO ITRR ZXDW X LZXALW OH MWVRWATUZ TOUWRB XAK LHAOTAPW ZWXROZS FMHIOZ. OZW HVVHUTOW TO OMPW YWLXPUW TB OZW
FMXUU TU RWBO OH FMHI HPO QHMW OZXA TO TU UPVVHUWK OH, OZW XMWX YWLHQWU OHH “YPUZS” XAK LXAAHO YW PUWK BHM LHIU. X
BXMQWM, IZH TU OXJTAF LXMW HB ZTU XATQXRU XAK OZWTM BHHK, ITRR MHOXOW OH QXJW UPMW OZW XATQXRU XMW QHDWK OH X AWI
VXOLZ HB FMXUU XAK OZTU QXJWU BHM YWUO MWUPROU BHM FMXUU, XATQXRU XAK VWHVRW (VHRRXA, 2007)."""
cipher = cipher

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

        D.swap2(c1, c2)
        
    except:
        continue

    print("Updated\n", end=" ")
    print(D.CipherText)
    print()

    




         

