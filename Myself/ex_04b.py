#!/usr/bin/python3

"""
    Script  : ex_04.py
    Author  : Mohamed Mukthar Ahmed
    Date    : 13-May-2019
    Purpose : Demo - The 'while' statement
                     Generate a multiplication table.
                     The 'for' statement
                     The 'range()' function
                     Nested Loop concept

"""

while True:
    number = int( input('Table of :') )
    for counter in range(1,11):
        product = number * counter
        print(number,"x",counter,"=",product)

    # Ask for continuation
    again = input('Continue [Y/N] :')
    if again in 'Nn':
        break

print("That's It!!!")




