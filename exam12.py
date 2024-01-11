def calculate_net_salary(gross_salary):
    #assuming deduction for tax and other expence 
    tax_percentage = 0.10 
    other_deduction = 1000
    tax_amount = (gross_salary * tax_percentage)
    net_salary = (gross_salary - tax_amount - other_deduction)
    return net_salary

def main():
    #input the gross salary of person
    gross_salary = float(input("enter the gross salary:"))

#calculate net salary using
net_salary = calculate_net_salary("gross_salary")
print("the net salary a person is:",(net_salary))
for name in range(main):
    main()
