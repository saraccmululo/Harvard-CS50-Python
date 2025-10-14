def convert(m):
    return m*(300000000*300000000)


mass = int(input("m:"))
energy = convert(mass)

print(f"E:{energy}")
