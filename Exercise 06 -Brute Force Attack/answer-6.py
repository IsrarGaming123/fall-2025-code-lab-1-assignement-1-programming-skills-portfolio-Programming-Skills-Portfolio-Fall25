# Define the correct password
CORRECT_PASSWORD = "12345"
# Maximum number of attempts allowed
MAX_ATTEMPTS = 5

# Initialize attempt counter
attempts = 0

# Display welcome message
print("=" * 50)
print("PASSWORD ENTRY SYSTEM")
print("=" * 50)

# While loop to repeatedly ask for password
while attempts < MAX_ATTEMPTS:
    # Get password input from user
    password = input("\nEnter password: ")
    
    # Check if password is correct
    if password == CORRECT_PASSWORD:
        print("\n✓ Access Granted! Welcome to the system.")
        break
    else:
        # Increment attempt counter
        attempts += 1
        
        # Calculate remaining attempts
        remaining = MAX_ATTEMPTS - attempts
        
        # Check if maximum attempts reached
        if remaining > 0:
            print(f"✗ Incorrect password. You have {remaining} attempt(s) remaining.")
        else:
            print("\n" + "!" * 50)
            print("✗ Maximum attempts reached!")
            print("The authorities have been alerted.")
            print("!" * 50)