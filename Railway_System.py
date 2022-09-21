print("Welcome to reservation system")
name = "ABC"
mobile = 12345
start = "Mumbai"
end = "Delhi"
date1 = 112233
date2 = 223344


option = int(input("What would you like to do: \n1.Reservation Form\n2.Ticket Info\n3.Ticket Cancellation\n4.Exit\nEnter Here: "))
if option == 1:
    name = input("Enter Your Name: ")
    mobile = int(input("Enter Your Mobile Number: "))
    start = input("Starting Point: ")
    end = input("Final Desitination: ")
    date1 = int(input("Start Date in form DDMMYY: "))
    date2 = int(input("End Date in form DDMMYY: "))
elif option == 2:
    id = int(input("Enter your ID: "))
    if id == 9876:
        print(f"Name: {name}\nModbile: {mobile}\nStarting Point: {start}\nFinal Desitination: {end}\nStart Date: {date1}\nEnd Date: {date2}")
    else:
        print("Enter Correct Pin")
elif option == 3:
    id = int(input("Enter your ID: "))
    if id == 9876:
        print("Ticket Cancelled")
    else:
        print("Enter Correct Pin")
elif option == 4:    
    print("Thank You")