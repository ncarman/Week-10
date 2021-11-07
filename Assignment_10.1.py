# Noah Carman
# CIS245
# November 6, 2021

# Importing the OS Path Module
import os.path

# Static Text
welcome_message = "Welcome!"
goodbye_message = "Thank you!"

# Initial inputs from user for file path and file name
print(welcome_message)
print()
file_path = input("Enter the path you would like to save to. If it does not exist, it will be created: ")
file_name = input("Enter the name of the file. It will be created in a moment at the chosen path: ")

# Creates the path if it does not exist
# Code Source: https://www.tutorialspoint.com/How-can-I-create-a-directory-if-it-does-not-exist-using-Python
if not os.path.exists(file_path):
    os.makedirs(file_path)

# Combines File Path and File Name Into String
path_and_name = os.path.join(file_path, file_name + ".txt")

# Opens the file in write mode
write_mode = open(path_and_name, "w")

# Obtains data from the user
print()
name = input("Enter your name: ")
address = input("Enter your address: ")
phone_number = input("Enter your phone number: ")

# Writes data to the file
write_mode.write(name + "," + address + "," + phone_number)
write_mode.close()

# More Static Text
information = f"The following information was recorded to {path_and_name}:"

# Opens the file in read mode
read_mode = open(path_and_name, "r")

# Prints the final information
print()
print(information)
print(read_mode.read())
print()
print(goodbye_message)