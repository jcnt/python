"""
CodingChallengesFYI https://github.com/CodingChallengesFYI

head.py
write a program that does the same as the unix "head"
"""

import sys


def read_stdin():
    """read stdin and return as a list"""
    stdin = []
    for line in sys.stdin:
        stdin.append(line)
    return stdin


print(len(sys.argv))
