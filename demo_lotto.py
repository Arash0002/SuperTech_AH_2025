#! /usr/bin/env python3
# Author: Arash
# Description: This script will demo
"""
    Docstring:
"""
import random

lotto = [] #Create empty list

while len(lotto) < 6:
    num = random.randint(1,60)
    if num in lotto:
        print("Duplciate number = ", num)
    else:
        lotto.append(num)

print("Lottery numbers are ", lotto)