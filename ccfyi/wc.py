"""
CodingChallengesFYI https://github.com/CodingChallengesFYI

wc.py
write a program that does the same as the unix "wc"
"""

import os
import sys


def read_stdin():
    """read stdin and return as a list"""
    stdin = []
    for line in sys.stdin:
        stdin.append(line)
    return stdin


def read_file(inputfile):
    """open file and return as a list"""
    with open(inputfile, "r") as file:
        return file.read().splitlines()


def arg_L(s):
    """provide the longest line within the input"""
    stdin_max = max(s)
    print(f"       {len(stdin_max.encode("utf-8"))}")


def arg_c(s):
    """count the number of the characters of stdin"""
    c = 0
    for line in s:
        c += len(line)
    return c


def arg_l(s):
    """count the number of the lines of stdin"""
    return len(s)


def arg_m(s):
    """count the number of the bytes of stdin"""
    m = 0
    for line in s:
        m += len(line.encode("utf-8"))
    return m


def arg_w(s):
    """count the number of the words of stdin"""
    w = 0
    for line in s:
        w += len(line.split())
    return w


def noarg(s):
    print("this is noarg")


arglist = ["-L", "-c", "-l", "-m", "-w"]
print(sys.argv)

if len(sys.argv) == 1:
    noarg("test")
elif sys.argv[1] in arglist:
    if sys.argv[-1] == "-L":
        si = read_stdin()
        arg_L(si)
    else:
        if os.path.exists(sys.argv[-1]):
            ri = read_file(sys.argv[-1])
            arg_L(ri)
        else:
            print(f"{sys.argv[0]}: {sys.argv[-1]}: No such file or directory")
