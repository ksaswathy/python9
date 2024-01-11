def exp_program(value):
    try:
      num=int(input("enter the number:"))
      return num
    except ValueError:
       print("error : invalidinput,input a valid integer")
exp_program("abc")




