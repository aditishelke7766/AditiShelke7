
import requests
from requests.exceptions import JSONDecodeError

def PartialUpdate():

        BookingId = num = int(input("Enter Booking id to Update the details -  "))

        PartialUpdateURL = f'https://restful-booker.herokuapp.com/booking/{BookingId}'


        AttrName = input("Which attribute you want to update from your details")


        header = {

            "Authorization" : "Basic YWRtaW46cGFzc3dvcmQxMjM="
        }

        data ={

        }

        if AttrName=="firstname":

            firstname = input("Enter updated first name")
            data = {
                "firstname" : firstname,
            }
        elif AttrName=="lastname":
            lastname = input("Enter updated Last name ")
            data = {
                "lastname" : lastname,
            }

        try:
            response = requests.patch(PartialUpdateURL,headers=header,json=data)

            response.raise_for_status()
            print("Record updated -- These are your updated details")

            result=response.json()
            print(result)

        except requests.exceptions.HTTPError as err:
            print(f"Failed to delete resource with ID {BookingId}. HTTP Error: {err}")
        except requests.exceptions.RequestException as err:
            print(f"Failed to delete resource with ID {BookingId}. Request Exception: {err}")
        except JSONDecodeError:
            print(f"Failed to delete resource with ID {BookingId}. Invalid JSON response.")



