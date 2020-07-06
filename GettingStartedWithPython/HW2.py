#3.1 Write a program to prompt the user for hours and rate per hour using input to compute gross pay. 
# Pay the hourly rate for the hours up to 40 and 1.5 times the hourly rate for all hours worked above 40 hours. 
# Use 45 hours and a rate of 10.50 per hour to test the program (the pay should be 498.75). 
# You should use input to read a string and float() to convert the string to a number. 
# Do not worry about error checking the user input - assume the user types numbers properly.

hours = input("Enter Hours: ")
rate = input("Enter rate: ") 
h = float(hours)
r = float(rate)

if h>40:
    rextra = float(rate)*1.5
    extra = h-40
    pextra = extra*rextra
    pay = pextra+40*r
    print(pay)

