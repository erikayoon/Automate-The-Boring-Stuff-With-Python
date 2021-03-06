# Chapter 6 - Bullet Point Adder
# Add bullet points to the beginning of each line of text

"""
Steps
1. Paste text from clipboard
2. Do something to it
3. Copy the new text to the clipboard
"""

import pyperclip

text = pyperclip.paste()

# Separate lines and add stars
lines = text.split('\n')
for i in range(len(lines)):
    lines[i] = '* ' + lines[i]

text = '\n'.join(lines)

pyperclip.copy(text)