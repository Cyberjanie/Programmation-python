people = {
    "janie": "555-1234",
    "bob": "555-5678",
    "alice": "555-8765" 
}   # Dictionary mapping names to phone numbers (only 2 entries shown / would not work if more than 2 entries)

name = input("searcch for a name: ").lower()
if name in people:
    print(f"{name}'s number is {people[name]}")
else:
    print(f"Sorry, no entry for {name}")

    