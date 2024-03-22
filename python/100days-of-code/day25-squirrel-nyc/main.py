import pandas

squirrel = pandas.read_csv("NYC_Squirrel_Data_20240225.csv")
color = squirrel["Primary Fur Color"]

gray_sq_count = len(squirrel[squirrel["Primary Fur Color"] == "Gray"])
black_sq_count = len(squirrel[squirrel["Primary Fur Color"] == "Black"])
red_sq_count = len(squirrel[squirrel["Primary Fur Color"] == "Cinnamon"])

gray = 0 
black = 0
red = 0


for i in color: 
    if i == "Gray": 
        gray += 1
    elif i == "Black":
        black += 1 
    elif i == "Cinnamon": 
        red += 1

nycsqr = {
    "colors": ["Grey", "Black", "Red"],
    "amount": [gray, black, red]
}

nycsqr2 = {
    "colors": ["Grey", "Black", "Red"],
    "amount": [gray_sq_count, black_sq_count, red_sq_count]
}
sqrfmt = pandas.DataFrame(nycsqr)
sqrfmt2 = pandas.DataFrame(nycsqr2)
sqrfmt.to_csv("squirrel_colors.csv")
print(sqrfmt)
print(sqrfmt2)