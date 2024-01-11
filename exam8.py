unit=int(input("enter the unit consumed:"))
if unit<=100:
    print("no charge for this user")
if 100<=unit<=200:
    amount=unit-100*5
    print("bill amount=",amount)
elif unit>=200:
    amount=100*0+100*5+(unit-200)*10
    print("bill amount=",amount)
else:
    print("enterd the unit is invalid")
