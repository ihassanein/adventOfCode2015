# Day 1 Advent of Code 2015
# Started August 2018
# Coded in Python

# Initialize floor variable #
floor = 0
counter = 0

# Open input file to read #
with open("input.txt", "r") as data:
    while True:
        move = data.read(1)
        if move == '(':
            floor += 1
            counter += 1
        elif move == ')':
            floor -= 1
            counter += 1
        if floor < 0:
            break
    print counter
