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
    return len(stdin_max.encode("utf-8"))


def arg_c(s):
    """count the number of the characters of input"""
    c = 0
    for line in s:
        c += len(line)
    return c


def arg_l(s):
    """count the number of the lines of input"""
    return len(s)


def arg_m(s):
    """count the number of the bytes of input"""
    m = 0
    for line in s:
        m += len(line.encode("utf-8"))
    return m


def arg_w(s):
    """count the number of the words of input"""
    w = 0
    for line in s:
        w += len(line.split())
    return w


argd = {"-L": arg_L, "-c": arg_c, "-l": arg_l, "-m": arg_m, "-w": arg_w}

if len(sys.argv) == 1:
    si = read_stdin()
    print(f"      {arg_l(si)}      {arg_w(si)}      {arg_c(si)}")
elif sys.argv[1] in argd:
    if sys.argv[-1] in argd:
        si = read_stdin()
        print(f"      {argd[sys.argv[-1]](si)}")
    else:
        if os.path.exists(sys.argv[-1]):
            ri = read_file(sys.argv[-1])
            print(f"      {argd[sys.argv[1]](ri)}")
        else:
            print(f"{sys.argv[0]}: {sys.argv[-1]}: No such file or directory")
elif sys.argv[1] == sys.argv[-1]:
    if os.path.exists(sys.argv[1]):
        ri = read_file(sys.argv[1])
        print(
            f"      {arg_l(ri)}      {
                arg_w(ri)}     {arg_c(ri)} {sys.argv[1]}"
        )
    else:
        print(f"{sys.argv[0]}: {sys.argv[1]}: No such file or directory")
