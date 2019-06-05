#!/usr/bin/python3

"""
    Script  : ex_02.py
    Author  : Mohamed Mukthar Ahmed
    Date    : 13-May-2019
    Purpose : Demo - Input Output processing

"""

name = input('Enter your name :')
while True:
    try:
        age = int( input('Age please (in years) :') )
        break
    except ValueError:
        print("Oops! It is not an INTEGER. Try again...")

print(name, "Welcome to COSS.")
print("Have a wonderful learning experience!")
print("Next year you will be ", age+1, "years old.")


a = 125
b = 12.45
c = "Keya"

print("Integer = %d\nFloat = %f\nString = %s\n" %(a,b,c))


