name = "Angela"
new_list = [letter for letter in name]
print(new_list)


num_list = [n*2 for n in range(1, 5)]
print(num_list)

names = ["Alex", "Beth", "Caroline", "Dave", "Elanor", "Freddie"]
allcaps = [name.upper() for name in names]
print(allcaps)