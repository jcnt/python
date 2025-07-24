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


def read_file(inputfile):
    """open file and return as a list"""
    with open(inputfile, "r") as file:
        return file.read().splitlines()


def noarg(s):
    """No argument, default run, head -n 10"""
    for line in range(10):
        print(s[line])


def argn(s, n):
    """-n count, Print count lines of each of the specified files."""
    for line in range(n):
        print(s[line])


def argc(s, c):
    """-c bytes, Print bytes of each of the specified files."""
    i = 0
    while c > 0:
        if c > len(s[i]):
            print(s[i])
            i += 1
            c -= len(s[i])
        else:
            print(s[i][:c], end="", flush=True)
            c = 0


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
            print("usage: head [-n lines | -c bytes] [file ...]")

if len(sys.argv) == 3:
    # head -10 filename or head -n 10 pipe
    f = sys.argv[2]
    if os.path.exists(f):
        finput = read_file(f)
        if str.isdigit(sys.argv[1][1:]):
            argn(finput, int(sys.argv[1][1:]))
        else:
            print(f"{sys.argv[0]}: invalid option -- {sys.argv[1]}")
            print("usage: head [-n lines | -c bytes] [file ...]")
    else:
        stdinput = read_stdin()
        if sys.argv[1] == "-n":
            if str.isdigit(sys.argv[2]):
                argn(stdinput, int(sys.argv[2]))
            else:
                print(f"{sys.argv[0]}: illegal line count -- {sys.argv[2]}")
        elif sys.argv[1] == "-c":
            if str.isdigit(sys.argv[2]):
                argc(stdinput, int(sys.argv[2]))
            else:
                print(f"{sys.argv[0]}: illegal byte count -- {sys.argv[2]}")
        else:
            print(f"{sys.argv[0]}: invalid option -- {sys.argv[1]}")
            print("usage: head [-n lines | -c bytes] [file ...]")

if len(sys.argv) == 4:
    # head -n 10 filename
    f = sys.argv[3]
    if os.path.exists(f):
        n = sys.argv[2]
        finput = read_file(f)
        # head -n 10 filename
        if sys.argv[1] == "-n":
            # -n
            if str.isdigit(n):
                argn(finput, int(n))
            else:
                print(f"{sys.argv[0]}: illegal line count -- {sys.argv[2]}")
        elif sys.argv[1] == "-c":
            # -c
            if str.isdigit(n):
                argc(finput, int(n))
            else:
                print(f"{sys.argv[0]}: illegal byte count -- {sys.argv[2]}")
        else:
            print(f"{sys.argv[0]}: invalid option -- {sys.argv[1]}")
            print("usage: head [-n lines | -c bytes] [file ...]")
    else:
        print(f"{sys.argv[0]}: {sys.argv[3]}: No such file or directory")
