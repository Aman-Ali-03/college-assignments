# Write a Python program that stores the following details using variables:
# Basic Salary = ₹58,750, HRA = 22% of Basic Salary, DA = 15% of Basic
# Salary, Professional Tax = ₹2,500. Perform the following tasks: Calculate
# Gross Salary, Calculate Net Salary after deducting Professional Tax, Print all
# values using formatted print statements, Print the data type of Net Salary,
# Round Net Salary to two decimal places.

basic_salary = 58750
HRA = basic_salary * 0.22
DA = basic_salary*0.15
Professional_Tax = 2500

gross_salary = basic_salary+HRA+DA

net_Salary = gross_salary-Professional_Tax

print("Your basic salary: ",basic_salary)
print("Your HRA: ",HRA)
print("Your DA: ",DA)
print("Professional Tax: ",Professional_Tax)
print("Gross salary: ",gross_salary)
print("Net Salary: ",net_Salary)
print("Type of Net Salary: ",type(net_Salary))
print(f"Round of 2 Decimal places Salary: {net_Salary : .2f}")