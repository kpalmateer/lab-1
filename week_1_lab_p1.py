# Kyle Palmateer
# ITEC 2905
# Lab 1

# import datetime modules
from datetime import datetime

# get user input and store as name and month variables
name = input("What is your name? ")
month = input("What month were you born in? ")

# get the current month formatted like "August"
cur_month = str(datetime.today().strftime('%B'))

# print the current month, a greeting and the number of letters in the user's name
print("The current month is " + str(cur_month) + ".")
print("Hello, " + name + "!")
print("Your name has " + str(len(name)) + " letters.")

# if the current month matches the month the user entered, print a happy bday month message
if month == cur_month:
    print("Happy birthday month!")
