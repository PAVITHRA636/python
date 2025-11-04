#make a mini calculatore
a=int(input("Enter number a:"))
b=int(input("Enter number b:"))
operatore=input("add/sub/multiply/divide:")
if(operatore=="add"):
    print(a+b)
elif(operatore=="sub"):
    print(a-b)
elif(operatore=="multiply"):
    print(a*b)
elif(operatore=="divide"):
    print(a/b)
else:
    print("Invalid")
