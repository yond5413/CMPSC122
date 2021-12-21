import datetime
class Zipcode:
    def __init__(self,zipcode,geolocation,location,timezonediff,obseveDayLight):   # main class objects within class or inheirtance? Also needs timezone info
        self.zipcode = zipcode
        self.geolocation = geolocation
        self.location = location
        self.timezonediff = timezonediff
        self.observeDayLight = obseveDayLight # caste to boolean bool(


    def __str__(self):
        dnow = datetime.datetime.utcnow()
        dadj = datetime.datetime
        dadj = datetime.datetime(dnow.year,dnow.month,dnow.day,dnow.hour+self.timezonediff,dnow.minute,dnow.second)
        return ("{}\t{}\t{}\t{}\t{}".format(str(self.zipcode),str(self.geolocation),str(self.location),str(dadj),
        " Follows daylight savings" if bool(self.observeDayLight) == True else "Doesn't follow"))

class Geolocation:
    def __init__(self,latitude,longitude):
        self.latitude = latitude
        self.longitude = longitude

    def __str__(self):
        return("{}\t{}".format(str(self.latitude),str(self.longitude)))

class Location:
    def __init__(self,city,state):
        self.city = city
        self.state = state

    def __str__(self):
        return("{}\t{}".format(self.city,self.state))

