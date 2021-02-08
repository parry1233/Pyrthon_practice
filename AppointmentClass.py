class Appointment:
    def __init__(self,year,month,date,app_type):
        self.year = year # year value
        self.month = month # month value
        self.date = date # date value
        if(app_type=="M"):
            self.appType = "M"
        elif(app_type=="O"):
            self.appType = "O"
        else:
            print("Input error! Thus appointment will set to default (Onetime).")
            self.appType = "O"

    def display(self):
        if(self.appType=="O"):
            print("[",self.year,"/",self.month,"/",self.date,"] Appointment type: Onetime")
        elif(self.appType=="M"):
            for i in range(self.month,13):
                print("[",self.year,"/",i,"/",self.date,"] Appointment type: Monthly")
