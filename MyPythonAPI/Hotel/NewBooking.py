
#Get User details for Booking
import requests

def bookhotel():

        firstname = input("Enter your FirstName: ")
        lastname = input("Enter your LastName .")
        checkin = input("Enter your checkindate .")
        checkout = input("Enter your checkOUTdate .")
        depositpaid = True

        CreateURL = 'https://restful-booker.herokuapp.com/booking'

        #Create JSON Payload for POST  call

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

        response = requests.post(CreateURL,json=data)

        if response.status_code==200:
            result = response.json()
            print(result)
            if 'bookingid' in result :

                print("Your Booking is Confirmed")
                print("Here are your Booking Details ...")

                bookingId = result['bookingid']
                firstname = result['booking']['firstname']
                lastname = result['booking']['lastname']
                totalPrice = result['booking']['totalprice']
                depositpaid = result['booking']['depositpaid']
                checkin = result['booking']['bookingdates']['checkin']
                checkout = result['booking']['bookingdates']['checkout']

                print(f"Booking Id : {bookingId}")
                print(f"Customer Name : {firstname}  {lastname}")
                print(f"Price : {totalPrice}")
                print(f"CheckIn Date : {checkin}")
                print(f"CheckOut Date : {checkout}")
                print("Thanku !!!")

            else:
                print("Sorry Booking request is rejected !!")

