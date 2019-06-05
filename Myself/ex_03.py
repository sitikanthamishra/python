#!/usr/bin/python3

"""
    Script  : 
    Author  : Mohamed Mukthar Ahmed
    Date    : 13-May-2019
    Purpose : Demo - Selection control structure i.e. if...else

"""

marks = int( input('Enter subject marks [0-100] :') )

if marks >= 75:
    grade = 'E'
elif marks >= 60 and marks < 75:
    grade = 'A+'
elif marks >= 50 and marks < 60:
    grade = 'A'
elif marks >= 40 and marks < 50:
    grade = 'B'
elif marks >= 35 and marks < 45:
    grade = 'C'
else:
    grade = 'F'

print("Grade = ", grade)




