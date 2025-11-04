def practice_1_beginner():
"""
Beginner: Understanding why we need files
"""
print("\n" + "="*50)
print("EXERCISE 1.1: Save Your Name")
print("="*50)
# TODO 1: Get user's name
name = input("Enter your name: ")
# TODO 2: Open a file called "myname.txt" for writing
# Hint: Use open("myname.txt", "w")
file = None # Replace None with open() function
# TODO 3: Write the name to the file
# Hint: Use file.write(name)
# TODO 4: Close the file
# Hint: Use file.close()
print(f"Name '{name}' saved to myname.txt!")
# TODO 5: Read it back
# Open the file for reading with "r" mode
file = None # Replace with open() for reading
# Read the content
saved_name = None # Replace with file.read()
week7_lecture1.md 2025-10-02
4 / 30
# Close the file
print(f"Read back: '{saved_name}'")
# Run the exercise
practice_1_beginner()