def Even_or_odd():
    number = int(input("Enter a number: "))  #enter the number 
    if number % 2 == 0:
        print(f"{number} is even") # if number is even 
    else:
        print(f"{number} is odd") # if number is odd

# Call the function
Even_or_odd()


# the f"{number} replaces the variable with is value for example if number = 4 then it will print 4 is even :D