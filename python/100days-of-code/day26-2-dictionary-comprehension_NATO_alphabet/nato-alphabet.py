import pandas

nalpha = pandas.read_csv("nato_phonetic_alphabet.csv")
print(nalpha)

nalpha_fixed = {row.letter:row.code for (index, row) in nalpha.iterrows()}
print(nalpha_fixed)

to_convert = input("Enter your name: ").upper()

try: 
    
    converted = [ nalpha_fixed[letter] for letter in to_convert]
    print(converted)
except KeyError: 
    print("please letters only")
