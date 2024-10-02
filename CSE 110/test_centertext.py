import shutil

text = "Centered Text"

# Get the terminal width
terminal_width = shutil.get_terminal_size().columns

# Calculate the number of spaces needed on each side to center the text
left_padding = (terminal_width - len(text)) // 2

# Print the text with the calculated padding
print(" " * left_padding + text)