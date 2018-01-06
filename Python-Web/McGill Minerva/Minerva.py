import requests
import sys
import getpass
from MinervaAPI import *
def main():
    # Only works for @mail.mcgill.ca right now as I auto add the suffix if it isn't present
    email = input("Email or ID:")
    if "@mail.mcgill.ca" not in email and "260" not in email:
        email += "@mail.mcgill.ca"
    password = getpass.getpass("Password or pin:")
    
    preLogin = "https://horizon.mcgill.ca/pban1/twbkwbis.P_WWWLogin"
    loginUrl = "https://horizon.mcgill.ca/pban1/twbkwbis.P_ValLogin"
    print(email)
    # Use with to make sure the session is closed when we exit the with block
    with requests.session() as s:
        login = {
            'sid' : email,
            'PIN' : password
        }
            
        r = s.get(preLogin) # Get cookies before logging in
        r = s.post(loginUrl, data=login)
        cases = {
            1 : transcript
        }
        options = 0
        while options != 2:
            print("What would you like to do?")
            print("1. View transcript.")
            print("2. Quit.")
            optStr = input("Enter a number from 1-2: ")
            options=int(optStr)
            if options == 1:
                cases[options](s)
            elif options != 2:
                print("Invalid number, please try again.\n")

if __name__ == "__main__":
    main()
