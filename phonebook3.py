import csv

file = open("phonebook.csv", "a") # to open the file in append mode

name = input("Enter name: ")
phone = input("Enter phone number: ")

writer = csv.writer(file) # create a writer object / writer is a variable, could be anything writer is use as a convention
writer.writerow([name, phone]) # write a row to the file
file.close() # close the file



