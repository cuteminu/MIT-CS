#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 15:39:53 2021

@author: yangminwoo
"""

# User Inputs
annual_salary = float(input("Enter your annual salary : $"))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal : "))
total_cost = float(input("Enter the cost of your dream home : $")) 

# Variables 
current_savings = 0 # the amount you have saved so far. starting from 0
portion_down_payment = 0.25 # the portion of the cost needed for a down payment
r = 0.04 # an annual rate of investment
monthly_salary = annual_salary/12 # monthly salary
down_payment = total_cost * portion_down_payment # down payment cost
month = 0 # how many months needed. starting from 0

# Iterations
while current_savings < down_payment :
    month += 1
    current_savings += current_savings * r/12
    current_savings += monthly_salary * portion_saved
    
# Show Result
print("Number of months:", month)