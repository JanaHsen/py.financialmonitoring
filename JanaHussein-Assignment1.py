#1)All the inputs we need 
# the user must enter the salary first
nabihas_salary = int(input("Please enter your salary $  "))
#the user must specify the month of the salary
salary_month = input('Please enter the corresponding month ')

#Condition
if nabihas_salary<0:
    print('invalid input.Please restart the program.')

    #the user must input the percentage of savings, rent and electricity
else:
    savings_percent = int(input("Please enter the percentage for savings  "))
    if savings_percent<0 or savings_percent>=100:
        print("Percentage is not logical. Please restart the program.")
    else:
        rent_percent = int(input("Please enter the percentage for rent "))
        if rent_percent<0 or rent_percent>=100:
            print("Percentage is not logical. Please restart the program.")
        else:
            elect_percent = int(input("Please enter the percentage for electricity "))
            if elect_percent<0 or elect_percent>=100:
                print("Percentage is not logical. Please restart the program.")
            else:
                #2)Allocate the amounts

                saving_amount = (nabihas_salary* (savings_percent/100))

                rent_amount = (nabihas_salary * (rent_percent/100))

                elect_amount = (nabihas_salary * (elect_percent/100))

                #combine all the spendings and add them
                total_spent = saving_amount + rent_amount + elect_amount

                #what's left of the user's salary
                left_salary = nabihas_salary - total_spent

                #Estimate yearly costs
                annual_rent = 12 * rent_amount
                annual_elec = 12 * elect_amount

                #Estimate the square of the user's salary for fun
                extra_money = nabihas_salary ** 2

                #Calculate the additional savings
                additional_savings = int (input('Enter the monthly additional saving   '))#the amount of additional saving
                #the additional amount saved over a year
                annual_add_saving = additional_savings * 12 
                #the initial amount saved over a year
                total_annual_savings = saving_amount * 12   
                #the contribution the additional saved amount does to the initial one.
                divided_amount  = (annual_add_saving / total_annual_savings) * 100

                #3)Display
                print ('_____________________________________________________________________________________________________________________')
                print('Your', salary_month,"'s salary is", nabihas_salary,'$' )
                print('Save',savings_percent,'%  --->', saving_amount,'$')
                print('Your rent amount is',rent_percent, '% --->',rent_amount,'$')
                print('Your electricity amount is',elect_percent,'% --->',elect_amount,'$')
                print("Your total spendings for this month are",total_spent,'$')
                print("The remaing amount of your salary is",left_salary,'$')
                print("Your annual expenses for rent and electricity are",annual_rent,'$ and',annual_elec,'$ respectively')
                print("Your annual savings amount is",total_annual_savings,'$')
                print('In the case where you save an additional',additional_savings,'$ monthly, you will be contributing with',divided_amount,"% to your annual savings")
                print('In case you ever get rich and your salary gets squared, you will have', extra_money,'$')
                print ('_____________________________________________________________________________________________________________________')









