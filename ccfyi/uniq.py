"""
CodingChallengesFYI https://github.com/CodingChallengesFYI

uniq.py
write a program that does the same as the unix "uniq"
"""

import sys


def read_stdin():
    """read stdin and return as a list"""
    stdin = []
    for line in sys.stdin.read().splitlines():
        stdin.append(line)
    return stdin


def read_file(inputfile):
    """open file and return as a list"""
    with open(inputfile, "r") as file:
        return file.read().splitlines()


print(sys.argv)

"""
len 1 -> noarg stdin
len 2 -> noarg file, arg + stdin
len 3 -. arg file 

"""
