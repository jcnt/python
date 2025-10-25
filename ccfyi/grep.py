"""
CodingChallengesFYI https://github.com/CodingChallengesFYI

grep.py
write a program that does the same as the unix "grep"
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


argd = {
    "-c": argc,
    "-i": argi,
    "-o": argo,
    "-v": argv,
}
print(sys.argv)

if len(sys.argv) == 2 and "-" not in sys.argv[-1]:
    # grep pattern stdin
    si = read_stdin()
    noarg(si, sys.argv[1])
elif len(sys.argv) == 4 and os.path.exists(sys.argv[-1]):
    # grep -c pattern file
    fi = read_file(sys.argv[-1])
    argd[sys.argv[1]](fi, sys.argv[2])
elif len(sys.argv) == 3:
    if os.path.exists(sys.argv[-1]):
        # grep pattern file
        fi = read_file(sys.argv[-1])
        noarg(fi, sys.argv[1])
    elif "-" in sys.argv[1]:
        print("grep -c pattern stdin")
        si = read_stdin()
        argd[sys.argv[1]](si, sys.argv[2])
    else:
        print("Usage: grep [OPTION]... PATTERNS [FILE]...")
        print("Try 'grep --help' for more information.")
else:
    print("Usage: grep [OPTION]... PATTERNS [FILE]...")
    print("Try 'grep --help' for more information.")


"""
grep pattern stdin -> len 2 -> 1. 
grep pattern file -> len 3 + -1 path exist
grep -c pattern stdin -> len 3 
grep -c pattern file -> len 4 -> 2. 
"""
