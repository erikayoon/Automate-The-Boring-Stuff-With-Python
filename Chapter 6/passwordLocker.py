# Chapter 6 Guided Project - Password Locker
# Use one master password to unlock a password management program

PASSWORDS = {
    'email': 'This1saFak3Pa55w0rd',
    'blog': 'This1san0ther1',
    'luggage': '1M0r3'
}

import sys, pyperclip

if len(sys.argv) < 2:
    print('Usage: python passwordLocker.py [account] - copy account password')
    sys.exit()

account = sys.argv[1] # first command line arg is the account name

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print('Password for ' + account + ' copied to clipboard.')
else:
    print('There is no account named ' + account)


