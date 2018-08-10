# Day 1 Advent of Code 2015
# Started August 2018
# Coded in Python

floor = 0

with open("input.txt", "r") as data:
    while True:
        move = data.read(1)
        if move == '(':
            floor += 1
        elif move == ')':
            floor -= 1

        if not move:
            print "End of File"
            break

    print "You would be located on floor", floor
