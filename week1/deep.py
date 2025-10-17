user_input = input(
    "What is the Answer to the Great Question of Life, the Universe, and Everything? ")
lower_input = user_input.strip().lower()
if lower_input == "42" or lower_input == "forty-two" or lower_input == "forty two":
    print("Yes")
else:
    print("No")
