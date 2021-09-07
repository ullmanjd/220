"""
Name: Jacob Ullman
lab2.py
"""
import math


def sum_of_threes():
    upper = eval(input("Please enter an upper bound: "))
    total = 0
    for threes in range(3, upper + 1, 3):
        total = threes + total
        print(total)
    print("The total is: ", total)


def multiplication_table():
    count = 1
    for multiples in range(1, 11):
        print(
        1 * count, 2 * count, 3 * count, 4 * count, 5 * count, 6 * count, 7 * count, 8 * count, 9 * count, 10 * count)
        count = count + 1


def triangle_area():
    a = eval(input("Please enter the height: "))
    b = eval(input("Please enter the width: "))
    c = eval(input("Please enter the length: "))
    s = (a + b + c) / 2
    area1 = s * (s - a) * (s - b) * (s - c)
    area = math.sqrt(area1)
    print(area)


def sumSquares():
    lower = eval(input("Please enter a lower bound: "))
    higher = eval(input("Please enter a higher bound: "))
    sum = 0
    for squares in range(lower, higher + 1):
        sum = sum + squares * squares
    print(sum)


def power():
    base = eval(input("Please enter a base: "))
    exponent = eval(input("Please enter a exponent: "))
    answer = 1
    for tick in range(1, exponent+1):
        answer = answer * base

    print(base, " ^ ", exponent, " = ", answer)
