"""
Author:         Tim Smith
Description:    Calculate the Present Value required to achieve a Future value at an expected 
                rate of return over a given number of terms.
"""
print("Welcome to the Present Value Calculator!")
FV = float(input("Please enter the current value of the investment (FV): "))
r = float(input("Please enter the expected rate of return (r): "))
n= float(input("Please enter the number of terms invested (n):"))
print("The PV of a FV=", FV, "invested for n=",n,"terms at an expected rate of return r=",r, "is", FV / (1+r)**n)
print("Thank you for using the Present Value Calculator")