import UserAuthentication
import NewBooking
import DeleteBooking
import UpdateBooking
import ParticalBookingUpdate


print("****** WELCOME TO PALM RESORT ***********")
print("Please Login to with your PALM Account ")


UserAuthentication.loginmodule()

print("1 . New Booking ")
print("2 . Delete Existing Booking ")
print("3 . Update Existing Booking ")
print("4 . Update Partial details of Existing Booking ")
print("5 . Get your booking details by booking ID ")

choice = num = int(input("Enter your choice: "))

def switch_case(choice):
    if choice == 1:
            NewBooking.bookhotel()
    elif choice == 2:
            DeleteBooking.deleteBooking()

    elif choice == 3:
        UpdateBooking.updateBooking()

    elif choice == 4:
        ParticalBookingUpdate.PartialUpdate()

    elif choice == 5:
        ParticalBookingUpdate.PartialUpdate()
    else:
        print("Invalid option.")


switch_case(choice)



