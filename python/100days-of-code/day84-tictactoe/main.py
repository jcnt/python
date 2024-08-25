# assignment porgram for python scripting
# Day 84: write a CLI version of the Tic Tac Toe game

import os
import time

a = [" ", " ", " "]
b = [" ", " ", " "]
c = [" ", " ", " "]


def print_board():
    print()
    print(f"  {a[0]}|{a[1]}|{a[2]}")
    print("  -----")
    print(f"  {b[0]}|{b[1]}|{b[2]}")
    print("  -----")
    print(f"  {c[0]}|{c[1]}|{c[2]}")
    print()


def is_over():
    if a[0] == a[1] == a[2] and a[0] != " ":
        return "win"
    if b[0] == b[1] == b[2] and b[0] != " ":
        return "win"
    if c[0] == c[1] == c[2] and c[0] != " ":
        return "win"
    if a[0] == b[0] == c[0] and a[0] != " ":
        return "win"
    if a[1] == b[1] == c[1] and a[1] != " ":
        return "win"
    if a[2] == b[2] == c[2] and a[2] != " ":
        return "win"
    if a[0] == b[1] == c[2] and a[0] != " ":
        return "win"
    if a[2] == b[1] == c[0] and a[2] != " ":
        return "win"
    if " " not in a and " " not in b and " " not in c:
        return "draw"
    return "continue"


player = 1
running = True

while running:

    if player == 1:
        mark = "X"
    else:
        mark = "O"

    os.system("clear")
    print_board()

    print(f"You're playing as {mark}")
    row = input("Row: (A/B/C) ").lower()
    col = input("Column (1/2/3) ")

    if row == "" or col == "":
        print("Try again! Wrong row or column.")
        time.sleep(3)
    else:
        ind = int(col) - 1
        if eval(row)[ind] != " ":
            print("Try again! That field is already used.")
            time.sleep(3)
        else:
            eval(row)[ind] = mark
            player *= -1

    print_board()

    status = is_over()

    if status == "win":
        os.system("clear")
        print_board()
        print(f"The winner is {mark}")
        print()
        break

    if status == "draw":
        os.system("clear")
        print_board()
        print(f"It's a draw! Try again!")
        print()
        break
