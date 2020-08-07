"""
File name: copyfile
Author: Raphael Puente
Student ID: 301075627
File description: A script that will copy the content of a source file into a destination file
"""

#asking the user for the name of the source file 
sourceFile = input("Hello, I'll be copying the content of one txt file into another\nPlease tell me the name of the source file:")

#asking the user for the name of the destination file file
destinationFile = input("Thank you, now, please tell me the name of the file where you want to copy the content:")

#opening the source file as "read"
source = open(sourceFile,"r")

#opening the destination file as "write"
destination = open(destinationFile,"w") 

#for each line in my source file, i'm copying all into my destination file
for line in source.readlines():
    destination.write(line)




