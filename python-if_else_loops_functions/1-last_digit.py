#!/usr/bin/python3
import random


number = str(random.randint(-10000, 10000))

Last_Digit =  int(number[ -1:])

if Last_Digit > 5:
	print(f"The Last Digit of {number} is the string {Last_Digit} and is greater than 5")
elif Last_Digit ==0 :
	print(f"The Last Digit of {number} is the string {Last_Digit} and is 0")
else:
	print(f"The Last Digit of {number} is the string {Last_Digit} and is less than 6 and not 0")
