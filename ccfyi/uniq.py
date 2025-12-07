"""
CodingChallengesFYI https://github.com/CodingChallengesFYI

uniq.py
write a program that does the same as the unix "uniq"
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


def argc():
    """Precede each output line with the count of the number of times the line
    occurred in the input"""
    ...


def argd():
    """Output a single copy of each line that is repeated in the input."""
    ...


def argi():
    """Case insensitive comparison of lines."""
    ...


def argu():
    """Only output lines that are not repeated in the input."""
    ...


def argf():
    """Ignore the first num fields in each input line when doing comparisons"""
    ...


def args():
    """Ignore the first chars characters in each input line when doing comparisons."""
    ...


argd = {
    "-c": argc,
    "-d": argd,
    "-i": argi,
    "-u": argu,
    "-f": argf,
    "-s": args,
}
print(sys.argv)

if "-f" in sys.argv or "-s" in sys.argv:
    print("not ready yet")
else:
    if len(sys.argv) == 1:
        # uniq stdin


"""
len 1 -> noarg stdin
len 2 -> noarg file, arg + stdin
len 3 -> arg file

"""
