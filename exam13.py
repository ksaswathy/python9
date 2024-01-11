
#calculate tax amount
#input the gross salary of person
gross_salary = float(input("enter the gross salary:"))

def tax_amount(gross_salary,tax_percentage):
    return gross_salary*tax_percentage

print (tax_amount(gross_salary,0.10))

#calculculate net salary
def net_salary(gross_salary, tax_amount, other_deduction):
    return gross_salary-tax_amount-other_deduction

print(net_salary(gross_salary,44000,4000))



