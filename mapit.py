#!/usr/bin/env pythonw
import webbrowser, sys, pyperclip

sys.argv

# Check if command line arguments were passed
if len(sys.argv) > 1:
    # we know that the address has been passed
    address = ' '.join(sys.argv[1:])
else:
    address = pyperclip.paste()

# https://www.google.ae/maps/place/<ADDRESS>
webbrowser.open('https://www.google.ae/maps/place/' + address)
