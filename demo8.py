#. Get input for salary and age.If salary greater than or equal to 20000 or age less than or equal to 25, get input for required loan amount. If not print you are not eligible for loan.
#If required loan amount is less than or equal to 50,000 print You are eligible for loan. If it is greater than 50,000 print maximum loan amount is 50,000.
a=int(input("Enter the salary:"))
b=int(input("Enter the age:"))
if(a>=20000 or b<=25):
    c=int(input("Enter the requied loan amount:"))
    if(c<=50000):
        print("You are eligible for loan")
    elif(c>50000):
        print("Maximum loan amount is 50000")
else:
    print("You are not eligible for loan")
