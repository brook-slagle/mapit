#! python3

# mapIt.py - launches a map inthe browser using an address from the command line or clipboard. 

import webbrowser, sys, pyperclip
if len(sys.argv) > 1:
    # get the address from the command line. 
    address = ' '.join(sys.argv[1:])

else: 
    # get address from clipboard
    address = pyperclip.paste()

print(address)
webbrowser.open('https://www.google.com/maps/place/' + address)
