#create a list
list=[11,22,6,8,9]
n=len(list)
for i in range(0,n):
    for x in range(i+1,n):
        y=list[i]
        if list[i]>list[x]:
         list[i]=list[x]
         list[x]=y
print(list[-3])
