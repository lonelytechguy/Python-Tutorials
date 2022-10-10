# Creating a global variable
role = "Software Engineer"

# Print role outside the function
print("Role outside the function is: " + role)

def occupation():
    global role
    # Assigning new value to role variable
    role = "Photographer"
    # Print role inside the function
    print("Role inside the function is: " + role)

# Call the occupation function
occupation()

print(role)
