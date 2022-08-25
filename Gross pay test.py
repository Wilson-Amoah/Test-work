#Write a program to prompt the user for hours and rate per hour to compute gross pay.

#A code that computes gross pay

Hours = (input("How many hours do you work in a week? " ))
Hourly_wage = (input ('What is your hourly wage? '))

#Rewrite your pay program using try and except so that your program handles non-numeric input gracefully.

try:
    correct_hrs = float(Hours)
    correct_wage = float (Hourly_wage)
    print("Please hold on a sec")
    
   

except:
    correct_hrs = str(Hours)
    correct_wage = str(Hourly_wage)
    print("Error!")


# Rewrite your pay computation to give the employee 1.5 times the 
# hourly rate for hours worked above 40 hours.

#Wage computation for more than 40hrs of work
if str(correct_hrs) == str(Hours):
    print("You did not enter a numeric value for hours of work")

elif str(correct_wage) == str(Hourly_wage):
    print("You did not enter a numeric value for hourly wage")

elif correct_hrs > 40:
    Pay = float(40) *  float (Hourly_wage) + float(correct_hrs - 40)*1.5* float(Hourly_wage)
    print("Your wage is USD " + str(Pay))

elif correct_hrs<=40:
    Pay = float(Hours) * float(Hourly_wage)
    print("Your weeekly gross pay is USD " + str(Pay))

#Rewrite your pay computation with time-and-a-half for overtime and create a function called computepay which takes two parameters ( hours and  rate).

def computepay(correct_hrs, correct_wage):
    pay = correct_hrs * correct_wage
    return pay

Salary = computepay(45, 10)
print("For the compute pay function, ")
print(f"your pay is USD {pay}")
