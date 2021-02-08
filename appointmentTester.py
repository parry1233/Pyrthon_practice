from AppointmentClass import Appointment

app_list = []
while True:
    app = input("Please enter the date that you want to add an appointment.\n(type with unit like year-month-date)\n")
    app_data = [int(data) for data in app.split("-")]
    #print(app_data,type(app_data)) #check data type
    app_type = input("which type of appoinment is it?\n(type O if it is an onetime appointment while type M if it is a montly appointment)\n")

    appointment = Appointment(app_data[0],app_data[1],app_data[2],app_type)
    app_list.append(appointment)

    check = input("Continue? (Type Y to continue / type N to exist)\n")
    if(check == "N"):
        break

for singleApp in app_list:
    singleApp.display()
