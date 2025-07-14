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


def argn():
    """-n count, Print count lines of each of the specified files."""
    print("argn")


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
    arg = sys.argv[1]
    if os.path.exists(arg):
        finput = read_file(arg)
        noarg(finput)
    else:
        print("probably an arg")
    # head filename
    # or
    # head -10 piped

if len(sys.argv) == 3:
    print("3")
    # head -10 filename
    # or
    # head -n 10 piped

if len(sys.argv) == 4:
    print("4")
    # head -n 10 filename
