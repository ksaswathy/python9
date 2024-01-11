#write a program to accept percentage from the user and display the display the grade according to the following criteria
per=int(input("enter the input of percentage"))

if per>90:
    print("A")
    
elif per<=90 and per>80 :
    print("B")

elif per<=80 and per>=60:
 print("C")

elif per < 60:
    print("D")