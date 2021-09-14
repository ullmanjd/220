"""
Name: Jacob Ullman
lab3.py
"""


def average():
    grades = eval(input("Enter the number of grades: "))
    total = 0
    for hw in range(1, grades + 1):
        grade = eval(input("Enter your grade on HW" + str(hw) + ":"))
        total = grade + total

    print(total / grades)


def tip_jar():
    tips = 0
    for turn in range(1, 6):
        tip = eval(input("How much would you like to donate?"))
        tips = tips + tip
    print("Total donations collected: ", tips)


def newton():
    x = eval(input("What number should be approximated?"))
    improvements = eval(input("How many times should the approximation be improved?"))
    approx = x / 2
    for turn in range(1, improvements + 1):
        approx = (approx + x / approx) / 2
    print("Approximated square root of ", x, " is ", approx)


def sequence():
    terms = eval(input("How many terms are in the sequence?"))
    lowtohigh = ""
    pos = 0
    for turn in range(1, terms + 1):
        term = eval(input("Please input a term: "))
        if term >= pos:
            pos = term
            lowtohigh = lowtohigh + str(pos)
        else:
            pos = term
            lowtohigh = str(pos) + lowtohigh

    print(lowtohigh)

#the total product isn't working, asked for assistance in lab and we couldn't determine why
def pi():
    n = eval(input("How many terms are in the series?"))
    product = 1
    for i in range(0, n):
        num = (i + 1) % 2 + (i + 1)
        den = i % 2 + (i + 1)

        print(str(num) + "/" + str(den)) #This is here to show that the formulas are correct
        product = product * (num / den)
    print(product)
