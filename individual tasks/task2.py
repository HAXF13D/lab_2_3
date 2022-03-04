#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys


def check(s):
    s = s[:-1]
    if s[0] == '-':
        s = s[1:]
    s = s.replace('.', '', 1)
    if s.isdigit():
        return 1
    return 0


if __name__ == "__main__":
    summa = 0
    for line in sys.stdin:
        if line == '\n':
            exit(0)
        elif check(line) == 1:
            summa += float(line)
        print(summa)
