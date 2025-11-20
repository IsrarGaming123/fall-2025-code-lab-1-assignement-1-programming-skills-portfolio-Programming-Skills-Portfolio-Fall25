score = 0 #setting initial score to 0
Capital_of_france = input("What is the capital of France? ")    #asking user for answer
if Capital_of_france.lower() == "paris": #checking if answer is correct 
    print("Correct!") #if correct, print correct and add 1 to score
    score += 1  #incrementing score by 1 
else:
    print("Incorrect. The capital of France is Paris.")


if Capital_of_Germany := input("What is the capital of Germany? ") == "Berlin":
    print("Correct!")
    score += 1
else:
    print("Incorrect. The capital of Germany is Berlin.")


if Capital_of_Italy := input("What is the capital of Italy? ") == "Rome":
    print("Correct!")
    score += 1  
else:
    print("Incorrect. The capital of Italy is Rome.")   


if Capital_of_Spain := input("What is the capital of Spain? ") == "Madrid":
    print("Correct!")
    score += 1
else:
    print("Incorrect. The capital of Spain is Madrid.") 
print(f"Your total score is {score} out of 4.")    