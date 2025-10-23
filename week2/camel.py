
s = input("camelCase: ")

snake_case = ""
for char in s:
    if char.isupper():
        lower_char = char.lower()
        new_char = "_"+lower_char
        snake_case = snake_case + new_char
    else:
        snake_case = snake_case+char

print("snake_case: ", snake_case)
