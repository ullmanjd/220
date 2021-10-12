# Jacob Ullman
# Lab 7
import math


def cash_conversion():
    number = eval(input("Please enter an integer to see the dollar value:"))
    print("$" + "{:.2f}".format(number))


def encode():
    message = (input("Please enter a message to encode:"))
    num = eval(input("Please enter an integer key:"))
    encoded = ""
    for i in message:
        encoded = encoded + chr(ord(i) + num)
    print(encoded)


def sphere_area():
    radius = eval((input("Please enter the radius of the sphere:")))
    r2 = radius * radius
    area = 4 * math.pi * r2
    print(area)


def sphere_volume():
    radius2 = eval((input("Please enter the radius of the sphere:")))
    r3 = radius2 * radius2 * radius2
    volume = 4 / 3 * math.pi * r3
    print(volume)


def sum_n():
    n = eval((input("Please enter how many natural numbers you'd like to sum:")))
    sum = 0
    for i in range(0, n + 1):
        sum = sum + i
    print(sum)


def sum_n_cubes():
    n = eval((input("Please enter how many numbers you'd like to sum:")))
    sum = 0
    for i in range(0, n + 1):
        sum = sum + i * i
    print(sum)


def encode_better():
    message = input("Please enter a message to encode:")
    cipher = input("Please enter a cipher phrase:")
    encoded = ""
    for i in range(0, len(message)):
        e = ord(cipher[i])-97 + ord(message[i])
        encoded += chr(e)

    print(encoded)
