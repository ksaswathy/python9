
list=[1,3,4,6,88,0]
print("orginal list:",list)
n=len(list)
for i in range(0, n):
    for x in range(i+1, n):
        y=list[i]
        if list[i] > list[x]:
         list[i]=list[x]
         list[x]=y
      
print (list[-3])


