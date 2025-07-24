"""
CodingChallengesFYI https://github.com/CodingChallengesFYI

wc.py
write a program that does the same as the unix "wc"
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


def argc():
    """Print num lines of leading and trailing context surrounding each match."""
    ...


def argi():
    """Perform case insensitive matching.  By default, grep is case sensitive."""
    ...


def argo():
    """Prints only the matching part of the lines."""
    ...


def argv():
    """Selected lines are those not matching any of the specified patterns."""
    ...
