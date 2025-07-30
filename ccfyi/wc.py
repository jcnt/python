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
    """count the number of the characters of input"""
    c = 0
    for line in s:
        c += len(line)
    print(f"     {c}")


def arg_l(s):
    """count the number of the lines of input"""
    print(f"      {len(s)}")


def arg_m(s):
    """count the number of the bytes of input"""
    m = 0
    for line in s:
        m += len(line.encode("utf-8"))
    print(f"     {m}")


def arg_w(s):
    """count the number of the words of input"""
    w = 0
    for line in s:
        w += len(line.split())
    print(f"      {w}")


def noarg(s):
    l = arg_l(s)
    w = arg_w(s)
    c = arg_c(s)
    print(l, w, c)


#    print(f"      {l} {w} {c}")


argd = {"-L": arg_L, "-c": arg_c, "-l": arg_l, "-m": arg_m, "-w": arg_w}

if len(sys.argv) == 1:
    si = read_stdin()
    noarg(si)
elif sys.argv[1] in argd:
    if sys.argv[-1] in argd:
        si = read_stdin()
        argd[sys.argv[-1]](si)
    else:
        if os.path.exists(sys.argv[-1]):
            ri = read_file(sys.argv[-1])
            argd[sys.argv[1]](ri)
        else:
            print(f"{sys.argv[0]}: {sys.argv[-1]}: No such file or directory")
