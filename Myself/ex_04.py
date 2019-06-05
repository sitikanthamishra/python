#!/usr/bin/python3

"""
    Script  : ex_04.py
    Author  : Mohamed Mukthar Ahmed
    Date    : 13-May-2019
    Purpose : Demo - The 'while' statement
                     Generate a multiplication table.
"""

while True:
    number = int( input('Table of :') )
    counter = 1
    while counter <= 10:
        product = number * counter
        print(number,"x",counter,"=",product)
        counter += 1

    # Ask for continuation
    again = input('Continue [Y/N] :')
    if again == 'N' or again == 'n':
        break

print("That's It!!!")




