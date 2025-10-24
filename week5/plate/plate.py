
import string

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    upper_s = s.upper()
    return max_min(upper_s) and start(upper_s) and num(upper_s) and no_punct(upper_s)


def start(s):
    if len(s) >=2 and s[0].isalpha() and s[1].isalpha():
        return True
    return False


def max_min(s):
    return 2 <= len(s) <= 6


def num(s):
    #for i in range(len(s)):
        #if s[i] == "0" and i !=len(s)-1:
            #return False
        #if s[i].isdigit() and i < len(s)-1:#keep i in-bound when checking s[i+1]
            #if s[i+1].isalpha():
                #return False
    #return True

    for i in range(len(s)):
        if s[i].isdigit():
            if i>1 and s[i-1].isalpha():#find the 1st digit. If it's 0, return false
                if s[i] =="0":
                    return False
            if i < len(s)-1 and s[i+1].isalpha():#check if next element after digit is letter. i < len(s)-1: keep i in-bound when checking s[i+1]
                    return False
    return True

def no_punct(s):
    for char in s:
        if char in string.punctuation:
            return False
    return True

if __name__ == "__main__":
    main()
