# Create a global variable outside a function
role = 'Software Engineer'

def position():
  # Print role inside the function
  print('Role is ', role)

# Call the function
position()

# Print role outside the function
print('Role is ', role)
