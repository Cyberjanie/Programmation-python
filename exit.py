import sys                          # to use sys.argv in the python library

if len(sys.argv) != 2:                  # != means does not equal
    print("Missing command line argument")
    sys.exit(1)                        # exit the program with error code 1

else:
    print("Hello, " + sys.argv[1])      # sys.argv[0] is the script name
    sys.exit(0)                        # exit the program with success code 0




# learning points:
# - how to use sys.argv to get command line arguments
# - how to use sys.exit() to exit the program with a specific exit code
# - the convention of using exit code 0 for success and non-zero for errors
