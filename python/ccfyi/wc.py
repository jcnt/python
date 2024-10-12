"""
CodingChallengesFYI https://github.com/CodingChallengesFYI

wc.py
write a program that does the same as the unix "wc"
"""

import sys


def readstdin():
    """read stdin and return as a list"""
    stdin = []
    for line in sys.stdin:
        stdin.append(line)
    return stdin


def filetostdin():
    pass


def arg_ll():
    pass


def arg_c(stdin):
    """count the number of the characters of stdin"""
    c = 0
    for _, line in enumerate(stdin):
        c += len(line)
    return c


def arg_l(stdin):
    """count the number of the lines of stdin"""
    return len(stdin)


def arg_m():
    pass


def arg_w(stdin):
    """count the number of the words of stdin"""
    w = 0
    for _, line in enumerate(stdin):
        w += len(line.split())
    return w


stdinput = readstdin()

if len(sys.argv) == 1:
    print(
        f"      {arg_l(stdinput)}\
     {arg_w(stdinput)}\
    {arg_c(stdinput)}"
    )

elif sys.argv[1] == "-l":
    print(f"      {arg_l(stdinput)}")

elif sys.argv[1] == "-c":
    print(f"      {arg_c(stdinput)}")

elif sys.argv[1] == "-w":
    print(f"     {arg_w(stdinput)}")

elif sys.argv[1] == "-m":
    print("-m")

elif sys.argv[1] == "-ll":
    print("-ll")

else:
    print("parameter is a file")
