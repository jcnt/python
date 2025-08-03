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


def argi():
    """Perform case insensitive matching.  By default, grep is case sensitive."""
    ...


def argo():
    """Prints only the matching part of the lines."""
    ...


def argv():
    """Selected lines are those not matching any of the specified patterns."""
    ...


def noarg(s, p):
    """selecting lines that match one or more patterns."""
    for line in s:
        if p in line:
            print(line)


fi = read_file(sys.argv[2])
argc(fi, sys.argv[1])
