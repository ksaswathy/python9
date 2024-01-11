a=int(input("enter a numbe:"))
b=int(input("enter a number:"))
try:
    c=a/b
except:
    c=a/(b+2)
    print("division by zero not permitted")
else:
    print("no exceptions generated")
finally:
    print("result",c)
    