s = input("Input: ")

twttr = ""
for char in s:
    if char in "aeiou" or char in "AEIOU":
        continue
    else:
        twttr += char

print("Output: ", twttr)
