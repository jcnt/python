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


print(sys.argv)

if "-n" in sys.argv:
    n = sys.argv[sys.argv.index("-n") + 1]
    if str.isdigit(n):
        if len(sys.argv) == 3:
            si = read_stdin()
            argn(si, int(n))
        else:
            fi = read_file(sys.argv[3])
            argn(fi, int(n))

elif "-c" in sys.argv:
    n = sys.argv[sys.argv.index("-c") + 1]
    if str.isdigit(n):
        if len(sys.argv) == 3:
            si = read_stdin()
            argc(si, int(n))
        else:
            fi = read_file(sys.argv[3])
            argc(fi, int(n))

else:
    if len(sys.argv) == 1:
        si = read_stdin()
        noarg(si)
    else:
        if "-" in sys.argv[1]:
            ...
