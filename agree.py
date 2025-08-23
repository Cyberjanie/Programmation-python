answer = input("do you agree? (yes/no): ")
if answer.lower() in ["yes", "y"]:
    print("You agreed!")    
elif answer.lower() in ["no", "n"]:
    print("You disagreed!")
else:
    print("Invalid input, please answer with 'yes' or 'no'.")
#!/usr/bin/env python3
# This script prompts the user for input and responds based on their answer.    