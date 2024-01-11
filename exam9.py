#write a program to check whether the last digit pf a number is divisible by 3 or not
num=int(input("enter the input number:"))
last_digit=num%10 
if last_digit%3==0:
    print("{} is divisible by 3".format (last_digit))
else:
    print("{} is not divisible by 3".format(last_digit))
