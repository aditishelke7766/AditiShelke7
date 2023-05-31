import requests
from requests.exceptions import JSONDecodeError

def deleteBooking():

        BookingId = num = int(input("Enter Booking id to delete -  "))

        DeleteURL = f'https://restful-booker.herokuapp.com/booking/{BookingId}'     #The f before a string in Python denotes an f-string or a formatted string literal. It allows you to embed expressions inside curly braces {} within the string, which are evaluated and replaced with their corresponding values.

        data = {
            "Authorization" : "Basic YWRtaW46cGFzc3dvcmQxMjM="
        }

        response = requests.delete(DeleteURL, headers=data)        # If we want to send cookie and authorization details we use header parameter

        try:
            response.raise_for_status()
            print(f"Booking with ID {BookingId} deleted successfully.")
        except JSONDecodeError:
            print(f"Failed to delete resource with ID {BookingId}. Invalid JSON response.")
        except requests.exceptions.HTTPError as err:
            print(f"Failed to delete resource with ID {BookingId}. HTTP Error: {err}")
        except requests.exceptions.RequestException as err:
            print(f"Failed to delete resource with ID {BookingId}. Request Exception: {err}")

