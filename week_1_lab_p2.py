# Kyle Palmateer
# ITEC 2905
# Lab 1

# create an empty list to hold the class list
class_list = []

# ask if user wants to add a class
add_class = input("Add a class to the list? Y/N ")

# if the user responds Y, ask the class name
while add_class == "Y":
    class_name = input("What is your class? ")
    # add the class to the list
    class_list.append(class_name)
    # print the class list to verify it was added
    print(class_list)
    # ask if user wants to add another class
    add_class = input("Add another class? Y/N ")

# if the user says no, print the class list
print(class_list)

# print each item in the list separately
for class_name in class_list:
    print(class_name)