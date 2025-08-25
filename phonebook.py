people = [
    {"name": "Janie", "phone": "555-1234"}, 
    {"name": "Bob", "phone": "555-5678"},   
    {"name": "Alice", "phone": "555-8765"}, 
]
name = input("Enter a name: ") # get the name to look for
for person in people: # look for the person
    if person["name"].lower() == name.lower(): # case insensitive match
        print(f"{person['name']}'s phone number is {person['phone']}.")# found
        break # exit the loop
else:
    print(f"Sorry, no entry found for {name}.") # not found

# learning point: the else clause on a for loop runs if the loop completes normally (no break)
# learning point: use .lower() to make string comparisons case insensitive
# learning dictionary: a data structure that stores key-value pairs, allowing for efficient lookups by key


