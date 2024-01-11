
num=int(input("enter thr number"))
if num==0:
    print("factorial of zero is 1")
else:
    pro=1
for i in range(num,1,-1):
    pro*=i
print(pro)

