#!/usr/bin/env python3
-# -*- coding: utf-8 -*-
"""
Created on Sun Feb 21 17:01:26 2021

@author: yangminwoo
"""

# Algorithms : Guess-And-Check, Approximate Solutions, Bisection Method

# Guess-And-Check

cube = 512

for guess in range(abs(cube)+1) :
    if guess ** 3 >= abs(cube) :
        break
if guess ** 3 != abs(cube) :
    print(cube, "is not a perfect cube number.")
else:
    if cube < 0 :
        guess = -guess
    print(guess, "is the cube root number of", cube)
    
# Approximate Solutions : guess, epsilon, increment

cube = 27
guess = 0.0
epsilon = 0.1
increment = 0.01
num_guesses = 0

while abs(guess**3-cube) >= epsilon and guess ** 3 <= cube :
    guess += increment
    num_guesses += 1
print("num_guesses:",num_guesses)
if abs(guess**3 - cube) >= epsilon :
    print("Failed on cube root of", cube)
else :
    print(guess,"is close to the cube root of", cube)

# Bisection Search : epsilon, low, high, guess

cube = float(input("What is the number of which you want to know the cube root? "))
epsilon = 0.01
negative = False

if cube < 0 : # When x is a negative value.
    negative = True
    cube = -cube
    
low = 0
if cube < 1 :
    high = 1
else :
    high = cube
guess = (low+high)/2.0
    

while abs(guess**3 - cube) >= epsilon :
    if guess ** 3 > cube :
        high = guess
    else :
        low = guess
    guess = (high + low) / 2.0

if negative :
    guess = -guess

print(guess,"is the cube root of", cube)