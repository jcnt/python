
rawnames = []

with open("Input/Names/invited_names.txt") as file:
    rawnames = file.read()

print(rawnames)
names=rawnames.split()
print(names)

with open("Input/Letters/starting_letter.txt") as file:
    origletter = file.read()

print(origletter)

for i in names:
    letter = origletter.replace("[name]", i)
    print(letter)

for i in names:
    letter = origletter.replace("[name]", i)
    with open(f"Output/ReadyToSend/{i}.txt", mode="w") as file:
       file.write(f"{letter}")
