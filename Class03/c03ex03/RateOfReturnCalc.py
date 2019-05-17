"""
Author:         Tim Smith
Description:    Calculate the required rate of return to achieve a given future value (FV) from a starting present value (PV)
                over a given number of terms.
"""
print("Welcome to the Rate of Return Calculator!")
FV = float(input("Please enter the target future value of the investment (FV): "))
PV = float(input("Please enter the current value of the investment (PV): "))
n= float(input("Please enter the number of terms invested (n):"))
print("The r of a FV=", FV, "of a present value PV=",PV, "invested for n=",n,"is", (FV/PV)**(1/n)-1)
print("Thank you for using the Present Value Calculator")