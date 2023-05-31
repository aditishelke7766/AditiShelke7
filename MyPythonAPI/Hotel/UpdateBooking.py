
import requests
from requests.exceptions import JSONDecodeError

def updateBooking():

        BookingId = num = int(input("Enter Booking id to Update the details -  "))    #need this conversion if you want to input number

        print("Enter Updated values for below details ..")
        firstname = input("Enter your FirstName: ")
        lastname = input("Enter your LastName .")
        depositpaid = True

        updateURL = f'https://restful-booker.herokuapp.com/booking/{BookingId}'

        data = {

            "firstname" : firstname,
            "lastname" : lastname,
            "totalprice" : 111,
            "depositpaid" :depositpaid,
            "bookingdates" : {
                "checkin" : "2018-01-01",
                "checkout" : "2019-01-01"
            },
            "additionalneeds" : "Breakfast"

        }

        header = {

            "Authorization" : "Basic YWRtaW46cGFzc3dvcmQxMjM="
        }

        try:
            response = requests.put(updateURL,json=data , headers = header)
            response.raise_for_status()       # Raise an exception for 4xx or 5xx status codes means success codes
            result=response.json()
            print(result)
            print(f"Booking Details updated successfully.")
        except JSONDecodeError:
            print(f"Failed to delete resource with ID {BookingId}. Invalid JSON response.")
        except requests.exceptions.HTTPError as err:
            print(f"Failed to delete resource with ID {BookingId}. HTTP Error: {err}")
        except requests.exceptions.RequestException as err:
            print(f"Failed to delete resource with ID {BookingId}. Request Exception: {err}")
