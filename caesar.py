# caesar.py
import string

def caesar(msg, shift_num=1):
    if msg == "":
        return "Please type a msg"
    letters = string.ascii_lowercase
    lettercaps = string.ascii_uppercase
    ##moves first character to last charcter
    mask = letters[shift_num:] + letters[:shift_num]
    maskcaps = lettercaps[shift_num:] + lettercaps[:shift_num]
    ##maps the charcters from alphabets A-Z or a-z to their corresponding shifted alphabets with help of Unicode
    ##print the mask and letters variable to get an idea 
    trantab = str.maketrans(letters, mask)
    #print(f"trantab={trantab}")    ##To see the unicode mapping
    trantabcaps = str.maketrans(lettercaps, maskcaps)
    trantab = trantab | trantabcaps ##combine the small and caps mapping 
    return msg.translate(trantab) ## Translate the msg based on the mapping
