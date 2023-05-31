import requests
import getpass

password = getpass.getpass("Enter your password: ")



# take username and password as input from user

def loginmodule():
    username = input("Enter your username: ")
    password = getpass.getpass("Enter your password: ")

    # here we are preparing our data as a josn payload to POST a request
    userdata = {
        "username": username,
        "password": password
    }

    AuthURL = 'https://restful-booker.herokuapp.com/auth'

    response = requests.post(AuthURL, json=userdata)  # Here we posted data to URL

    if response.status_code == 200:  # This means URL has responded you with something
        result = response.json()

        if 'reason' in result:
            print("User is not valid.")

        if 'token' in result:
            token = result['token']
            print(token)
            print("Authentication is Successfull !!")
    else:
        print("server Error.")
