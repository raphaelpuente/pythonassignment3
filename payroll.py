"""
File name: payroll
Author: Raphael Puente
Student ID: 301075627
File description: A script that reads the info from data.txt and outputs data into the console
"""

#importing information from data.txt
datafile = open("data.txt","r")

#printing the header
print(f"ID\tName\t\tHours worked")
print(f"-------------------------------------")

#looping each line inside of our txt file
for person in datafile:
    #splitting into 4 elements: id, last name, first name and hours worked
    (id,last,first,hours) = person.split(",")
    #printing it in the console
    print(f"{id}\t{first} {last}\t{hours}")