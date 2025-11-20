#name is the array 
Array_Name = ["Jake", "Zac", "Ian", "Ron", "Sam", "Dave"]

#searching if the name is in the list 
def search_name(search_term):
    for name in Array_Name:
        if name.lower() == search_term.lower():
            return True
    return False

#asking the user to input the name to be searched for 
user_search = input("Enter a name to search: ")

#Finding the name and outputs
if search_name(user_search):
    print(user_search + " was found in the list!")
else:
    print(user_search + " was not found in the list")