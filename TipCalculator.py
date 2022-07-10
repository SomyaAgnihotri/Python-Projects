print ("Welcome to the tip calculator")
total_bill = float (input ("what was the total bill? $"))
n = int(input("what percentage tip would you like to give? 10, 12 or 15? "))
tip_percentage = total_bill* (n/100)
new_bill = total_bill+tip_percentage
m = int (input ("How many people to split the bill? "))
each_person = (new_bill/m) 
a = round(each_person,2)
print (f"Each person should pay: ${a}")
