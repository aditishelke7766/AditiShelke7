import  requests
from requests.exceptions import JSONDecodeError

BookingId = num = int(input("Enter Booking id  -  "))

getDetailURL = f'https://restful-booker.herokuapp.com/booking/{BookingId}'

data = {
    "Authorization" : "Basic YWRtaW46cGFzc3dvcmQxMjM="
}


try:
    response = requests.patch(getDetailURL,headers=data)

    response.raise_for_status()
    print(f"Below are your record details for booking ID {BookingId} ")
    result=response.json()
    print(result)

except requests.exceptions.HTTPError as err:
    print(f"Failed to delete resource with ID {BookingId}. HTTP Error: {err}")
except requests.exceptions.RequestException as err:
    print(f"Failed to delete resource with ID {BookingId}. Request Exception: {err}")
except JSONDecodeError:
    print(f"Failed to delete resource with ID {BookingId}. Invalid JSON response.")