"""
CodingChallengesFYI https://github.com/CodingChallengesFYI

head.py
write a program that does the same as the unix "head"
"""

import sys
from os import walk


def read_stdin():
    """read stdin and return as a list"""
    stdin = []
    for line in sys.stdin:
        stdin.append(line)
    return stdin


def noarg():
    """No argument, default run, head -n 10"""
    print("noarg")


def argn():
    """-n count, Print count lines of each of the specified files."""
    print("argn")


def argc():
    """-c bytes, Print bytes of each of the specified files."""
    print("argc")


print(len(sys.argv))
print(sys.argv[0])

# 1 -> piped into
# 2 -> no arg just filename

if len(sys.argv) == 1:
    print("1")
    # no arg, piped, head -10

if len(sys.argv) == 2:
    print("2")
    # head filename
    # or
    # head -arg piped

if len(sys.argv) == 3:
    print("3")
    # head -arg filename
