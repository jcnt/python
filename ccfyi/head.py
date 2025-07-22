"""
CodingChallengesFYI https://github.com/CodingChallengesFYI

head.py
write a program that does the same as the unix "head"
"""

import os
import sys


def read_stdin():
    """read stdin and return as a list"""
    stdin = []
    for line in sys.stdin.read().splitlines():
        stdin.append(line)
    return stdin


def read_file(f):
    with open(f) as file:
        flist = file.read().splitlines()
    return flist


def noarg(s):
    """No argument, default run, head -n 10"""
    for line in range(10):
        print(s[line])


def argn(s, n):
    """-n count, Print count lines of each of the specified files."""
    for line in range(n):
        print(s[line])


def argc():
    """-c bytes, Print bytes of each of the specified files."""
    print("argc")


print("====================")
print("remove this part")
print(sys.argv)
print("====================\n")


if len(sys.argv) == 1:
    # no arg, piped, head -10
    stdinput = read_stdin()
    noarg(stdinput)

if len(sys.argv) == 2:
    # head filename or head -10 pipe
    f = sys.argv[1]
    if os.path.exists(f):
        finput = read_file(f)
        noarg(finput)
    else:
        if str.isdigit(sys.argv[1][1:]):
            stdinput = read_stdin()
            argn(stdinput, int(sys.argv[1][1:]))
        else:
            print(f"{sys.argv[0]}: invalid option -- {sys.argv[1]}")

if len(sys.argv) == 3:
    # head -10 filename or head -n 10 pipe
    f = sys.argv[2]
    if os.path.exists(f):
        finput = read_file(f)
        if str.isdigit(sys.argv[1][1:]):
            argn(finput, int(sys.argv[1][1:]))
        else:
            print(f"{sys.argv[0]}: invalid option -- {sys.argv[1]}")
    else:
        stdinput = read_stdin()
        if sys.argv[1] == "-n":
            if str.isdigit(sys.argv[2]):
                argn(stdinput, int(sys.argv[2]))
            else:
                print(f"{sys.argv[0]}: illegal line count -- {sys.argv[2]}")
        elif sys.argv[1] == "-c":
            argc()
        else:
            print("need usage info here")

if len(sys.argv) == 4:
    f = sys.argv[3]
    if os.path.exists(f):
        n = sys.argv[2]
        if str.isdigit(n):
            # head -n 10 filename
            if sys.argv[1] == "-n":
                # -n
                finput = read_file(f)
                argn(finput, int(n))
            elif sys.argv[1] == "-c":
                # -c
                argc()
            else:
                print("need usage info here")
        else:
            print(f"{sys.argv[0]}: illegal line count -- {sys.argv[2]}")
