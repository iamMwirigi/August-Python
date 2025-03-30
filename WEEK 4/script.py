# Step 1: Read input.txt
with open("input.txt", "r") as file:
    content = file.read()

# Step 2: Count words
word_count = len(content.split())

# Step 3: Convert text to uppercase
upper_text = content.upper()

# Step 4: Write processed text and word count to output.txt
with open("output.txt", "w") as file:
    file.write(f"Processed Text:\n{upper_text}\n")
    file.write(f"\nWord Count: {word_count}\n")

# Step 5: Print success message
print("✅ Processing complete! Check output.txt for results.")
