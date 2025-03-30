# Open input.txt in read mode
with open("input.txt", "r") as file:
    content = file.read()  # Read content

# Modify content (convert to uppercase)
modified_content = content.upper()

# Write modified content to output.txt
with open("output.txt", "w") as file:
    file.write(modified_content)

print("✅ File has been processed and saved as output.txt!")  
