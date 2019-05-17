"""
Author:         Tim Smith
Description:    Calculate the Future value of a present value invested at am expected 
                rate of return over a given number of terms.
"""
print("Welcome to the Future Value Calculator!")
PV = float(input("Please enter the current value of the investment (PV): "))
r = float(input("Please enter the expected rate of return (r): "))
n= float(input("Please enter the number of terms invested (n):"))
print("The FV of a PV=", PV, "invested for n=",n,"terms at an expected rate of return r=",r, "is", PV*(1+r)**n)
print("Thank you for using the Present Value Calculator")