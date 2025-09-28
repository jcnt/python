"""
CodingChallengesFYI https://github.com/CodingChallengesFYI

grep.py
write a program that does the same as the unix "grep"
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


def argA():
    """Print num lines of trailing context after each match."""
    ...


def argB():
    """Print num lines of leading context before each match."""
    ...


def argc(s, p):
    """Print num lines of leading and trailing context surrounding each match."""
    n = 0
    for line in s:
        if p in line:
            n += 1
    print(n)


def argi(s, p):
    """Perform case insensitive matching.  By default, grep is case sensitive."""
    for line in s:
        if p.lower() in line.lower():
            print(line)


def argo(s, p):
    """Prints only the matching part of the lines."""
    for line in s:
        if p in line:
            print(p)


def argv(s, p):
    """Selected lines are those not matching any of the specified patterns."""
    for line in s:
        if p not in line:
            print(line)


def noarg(s, p):
    """selecting lines that match one or more patterns."""
    for line in s:
        if p in line:
            print(line)


print(sys.argv)
fi = read_file(sys.argv[len(sys.argv) - 1])
argo(fi, sys.argv[1])
