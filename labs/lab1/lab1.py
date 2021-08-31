"""
Name: <Jacob Ullman >
lab1.py

Problem: This function calculates the area of a rectangle
"""


def calc_rec_area():
    length = eval(input("Enter the length: "))
    width = eval(input("Enter the width: "))
    area = length * width
    print("Area =", area)

def calc_volume():
    length = eval(input("Enter the length: "))
    width = eval(input("Enter the width: "))
    height = eval(input("Enter the height: "))
    volume = length * width * height
    print("Volume = ", volume)

def shooting_percentage():
    total = eval(input("Enter the total shots: "))
    success = eval(input("Enter the shots made: "))
    percent = total/success
    print("Percentage of shots made = ", percent)

def coffee():
    pounds = eval(input("Enter the # of pounds: "))
    cost = 10.5*pounds+.86*pounds+1.5
    print("Cost = ", cost)

def kilometers_to_miles():
    kilometers = eval(input("Enter the kilometers traveled: "))
    miles = kilometers/1.61
    print("Miles traveled = ", miles)