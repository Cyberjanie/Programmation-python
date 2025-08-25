scores = []

for i in range(3):
    try:
        score = float(input("Score : ")) # int is used to convert input string to an integer
        scores.append(score) # append is used to add elements to a list
    except ValueError:
        print("Invalid input. Please enter a numeric value.")

average = sum(scores) / len(scores) # len is used to get the number of elements in a list (for a division)
print(f"Average score: {average:.1f}")


