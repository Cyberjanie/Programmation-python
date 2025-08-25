from sys import argv

if len(argv) == 2: # program will work only with one argument because argv[0] is the program name
    print(f" Hello, {argv[1]}!") # argv[1] is the first argument
else:
    print(" Hello, World !")


# to run the program, use the command line:
# python greet.py <name>    
# for example:
# python greet.py Janie will output "Hello, Janie!"
# python greet.py will output "Hello, World!"
# Janie is the first argument (argv[1]) passed to the program
