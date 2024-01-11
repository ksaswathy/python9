#write a program to accept the cost price of the bikethe road tax to be paid according to the following criteria
a=int(input("enter the cost price of bike"))

x=(a*15)/100
y=(a*10)/100
z=(a*5)/100

if a>100000:
    print(x)
elif a>50000:
    print(y)
elif a<=100000:
    print(y)
elif a<=50000:
    print(z)
