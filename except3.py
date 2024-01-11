def list_pgm(list1,index):
    try:
        print("the element is:",list[index])
    except IndexError as e:
        raise Exception("index is outof range",e)
    
limit=int(input("enter the limit:"))
list1=[]
for i in range(limit):
    number=int(input("enter numbers:"))
    list1.append(number)

print("list element are:",list1)
index=int(input("enter the index of element you want:"))
list_pgm(list1,index)