#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 19 15:51:16 2021

@author: yangminwoo

In Part B, you had a chance to explore how both the percentage of your salary that you save each month 
and your annual raise affect how long it takes you to save for a down payment.  This is nice, but
suppose you want to set a particular goal, e.g. to be able to afford the down payment in three years.
How much should you save each month to achieve this?  In this problem, you are going to write a 
program to answer that question.  To simplify things, assume:
31. Your semi­annual raise is .07 (7%)
2. Your investments have an annual return of 0.04 (4%)  
3. The down payment is 0.25 (25%) of the cost of the house 
4. The cost of the house that you are saving for is $1M.
You are now going to try to find the best rate of savings to achieve a down payment on a $1M house in 
36 months. Since hitting this exactly is a challenge, we simply want your savings to be within $100 of 
the required down payment. 
In ps1c.py​, write a program to calculate the best savings rate, as a function of your starting salary.
You should use bisection search​ to help you do this efficiently. You should keep track of the number of 
steps it takes your bisections search to finish. You should be able to reuse some of the code you wrote
for part B in this problem.  
Because we are searching for a value that is in principle a float, we are going to limit ourselves to two
decimals of accuracy (i.e., we may want to save at 7.04% ­­ or 0.0704 in decimal – but we are not 
going to worry about the difference between 7.041% and 7.039%).  This means we can search for an
integer​ between 0 and 10000 (using integer division), and then convert it to a decimal percentage
(using float division) to use when we are calculating the current_savings​ after 36 months. By using
this range, there are only a finite number of numbers that we are searching over, as opposed to the
infinite number of decimals between 0 and 1. This range will help prevent infinite loops. The reason we
use 0 to 10000 is to account for two additional decimal places in the range 0% to 100%. Your code
should print out a decimal (e.g. 0.0704 for 7.04%).
Try different inputs for your starting salary, and see how the percentage you need to save changes to
reach your desired down payment.  Also keep in mind it may not be possible for to save a down
payment in a year and a half for some salaries. In this case your function should notify the user that it 
is not possible to save for the down payment in 36 months with a print statement. Please make your
program print results in the format shown in the test cases below.   
Note: There are multiple right ways to implement bisection search/number of steps so your
results may not perfectly match those of the test case. 



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
