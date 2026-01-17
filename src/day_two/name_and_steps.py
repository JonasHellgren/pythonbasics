name = input("Vad heter du? ")
start = int(input("Starttal: "))
steps = int(input("Hur många steg? "))

print(f"Hej {name}!")

for i in range(steps):
    value = start + i
    print(f"Steg {i + 1}: {value}")

