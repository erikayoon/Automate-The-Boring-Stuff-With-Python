"""
Write a program that finds every phone number and email address in a long webpage or word doc. 
Perhaps a program that searches the text in your clipboard for phone numbers and email addresses, then
replaces the text with just the phone numbers and emails it finds. 
"""
# STEP 1: Import pyperclip and regex libraries/modules
import pyperclip, re

# STEP 2: Define regexes for what you are looking for
# Phone Number Regex
phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?              # area code
    (\s|-|\.)                       # separator
    \d{3}                           # first 3 digits
    (\s|-|\.)                       # separator
    \d{4}                           # last 4 digits
    (\s*(ext|x|ext.)\s*\d{2,5})?    # extension
)''', re.VERBOSE)

# Email Regex
emailRegex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+       # username
    @                       # @ symbol
    [a-zA-Z0-9.-]+          # domain name
    (\.[a-zA-Z]{2,4})       # dot something
)''', re.VERBOSE)

# STEP 3: Get text off of the clipboard
text = str(pyperclip.paste())

if text == '':
    print('There is nothing on your clipboard. Please copy something and try again.')   # Input validation
elif len(text) > 0:                             # if text is not empty, look for matches
    phoneMatches = []
    emailMatches = []
    for groups in phoneRegex.findall(text):     # Find phone matches and add to list
        phoneMatches.append(groups[0])
    for groups in emailRegex.findall(text):     # Find email matches and add to list
        emailMatches.append(groups[0])
    
    if len(phoneMatches) > 0 or len(emailMatches) > 0:   # If there are matches, paste it for the user
        if len(phoneMatches) > 0:
            phoneNumbers = '\n'.join(phoneMatches)           # Copy phone numbers
            pyperclip.copy(phoneNumbers)
            print("These are the phone numbers I found: ")
            print(pyperclip.paste())                         # Paste phone numbers
        if len(emailMatches) > 0:
            emails = '\n'.join(emailMatches)                 # Copy email addresses
            pyperclip.copy(emails)
            print("These are the email addresses I found: ")
            print(pyperclip.paste())                         # Paste email addresses
    else:                                       # If there were no matches, tell the user
        print('Sorry, there were no matches.')
