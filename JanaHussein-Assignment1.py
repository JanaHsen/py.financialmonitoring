#1)All the inputs we need 
# the user must enter the salary first
nabihas_salary = int(input("Please enter your salary  "))

#the user must specify the month of the salary
salary_month = input('Please enter the corresponding month ')

#the user must input the percentage of savings, rent and electricity
savings_percent = int(input("Please enter the percentage for savings  "))

rent_percent = int(input("Please enter the percentage for rent "))

elect_percent = int(input("Please enter the percentage for electricity "))

#2)Allocate the amounts

saving_amount = (nabihas_salary* (savings_percent/100))

rent_amount = (nabihas_salary * (rent_percent/100))

elect_amount = (nabihas_salary * (elect_percent/100))

#combine all the spendings and add them
total_spent = saving_amount + rent_amount + elect_amount

#what's left of the user's salary
left_salary = nabihas_salary - total_spent



