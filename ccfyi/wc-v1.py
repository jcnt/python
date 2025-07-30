"""
first try, looks and feels horrible 

CodingChallengesFYI https://github.com/CodingChallengesFYI

wc.py
write a program that does the same as the unix "wc"
"""

import sys


def read_stdin():
    """read stdin and return as a list"""
    stdin = []
    for line in sys.stdin:
        stdin.append(line)
    return stdin


def arg_ll(stdin):
    """provide the longest line within the input"""
    stdin_max = max(stdin)
    return len(stdin_max.encode("utf-8"))


def arg_c(stdin):
    """count the number of the characters of stdin"""
    c = 0
    for line in stdin:
        c += len(line)
    return c


def arg_l(stdin):
    """count the number of the lines of stdin"""
    return len(stdin)


def arg_m(stdin):
    """count the number of the bytes of stdin"""
    m = 0
    for line in stdin:
        m += len(line.encode("utf-8"))
    return m


def arg_w(stdin):
    """count the number of the words of stdin"""
    w = 0
    for line in stdin:
        w += len(line.split())
    return w


if len(sys.argv) == 1:
    stdinput = read_stdin()
    print(
        f"      {arg_l(stdinput)}\
     {arg_w(stdinput)}\
    {arg_c(stdinput)}"
    )

if len(sys.argv) == 2:
    if sys.argv[1] == "-l":
        stdinput = read_stdin()
        print(f"      {arg_l(stdinput)}")

    elif sys.argv[1] == "-c":
        stdinput = read_stdin()
        print(f"    {arg_c(stdinput)}")

    elif sys.argv[1] == "-w":
        stdinput = read_stdin()
        print(f"     {arg_w(stdinput)}")

    elif sys.argv[1] == "-m":
        stdinput = read_stdin()
        print(f"    {arg_m(stdinput)}")

    elif sys.argv[1] == "-L":
        stdinput = read_stdin()
        print(f"     {arg_ll(stdinput)}")

    else:
        with open(sys.argv[1], "r", encoding="UTF8") as file:
            stdinput = file.readlines()
        # Indenting is off for print to get execlty the same output as wc
        print(
            f"      {arg_l(stdinput)}\
     {arg_w(stdinput)}\
    {arg_c(stdinput)} {sys.argv[1]}"
        )
