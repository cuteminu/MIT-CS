#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 19 15:51:16 2021

@author: yangminwoo
"""
# User Inputs
annual_salary = float(input("Enter your starting salary : $"))

# Variables 
current_savings = 0 # the amount you have saved so far. starting from 0
portion_down_payment = 0.25 # the portion of the cost needed for a down payment
r = 0.04 # an annual rate of investment
monthly_salary = annual_salary/12 # monthly salary
semi_annual_raise = .07
total_cost = 1000000
down_payment = total_cost * portion_down_payment # down payment cost
bisection_times = 0 # The number of bisection search iterations. Starting from 0

# Define Function returning current_savings

def diff_cur_savings(save_portion, current_savings, monthly_salary) :
    for month in range (36) :
        current_savings += current_savings * r/12
        current_savings += monthly_salary * save_portion
        if month % 6 == 0 :
            monthly_salary += monthly_salary * .07
    return current_savings - down_payment 

# Bisection Search
start = 0 # starting point of bisection search. starting from 0
end = 10000 # end point of bisection search. starting from 10000
saving_rate = 0

while diff_cur_savings(start * 0.0001, current_savings, monthly_salary) * diff_cur_savings(end * 0.0001, current_savings, monthly_salary) < 0 :
    mid = (start + end) / 2
    if abs(diff_cur_savings(mid * 0.0001, current_savings, monthly_salary)) == 0 or abs(diff_cur_savings(start * 0.0001, current_savings, monthly_salary) - diff_cur_savings(end * 0.0001, current_savings, monthly_salary))/2 < 100 : # 
        saving_rate = mid
        break
    elif diff_cur_savings(start * 0.0001, current_savings, monthly_salary) * diff_cur_savings(mid * 0.0001, current_savings, monthly_salary) < 0 : 
        end = mid
    else : 
        start = mid
    saving_rate = start + end /2
    bisection_times += 1

# Print Result
if bisection_times == 0 :
    print("It is not possible to pay the down payment in three years.")
else :
    print("Best savings rate:", saving_rate * 0.0001)
    print("Steps in bisection search:", bisection_times)
