# Define a function named "new_string" that takes a string parameter called "text"
def new_string(text):
    # Check if the length of the "text" is greater than or equal to 2 and if the first two characters of "text" are "Is"
    if len(text) >= 2 and text[:2] == "Is":
        # If the conditions are met, return the original "text" unchanged
        return text
    else:
        # If the conditions are not met, prepend "Is" to the "text" and return the modified string
        return "Is" + text

# Call the "new_string" function with the argument "Array" and print the result
print(new_string("Array"))

# Call the "new_string" function with the argument "IsEmpty" and print the result
print(new_string("IsEmpty"))