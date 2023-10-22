#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
print("Welcome to tip calculator")
bill = float (input("what was the total bill?"))
percent = int (input("what percentage would you like to spit the bill? 10,12 or 15?"))
split = int (input("how many people to split the bill?"))
new_percentage = percent /100
new_bill = new_percentage * bill
totals = (new_bill + bill)/split
print(totals)

