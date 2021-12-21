import csv
from zipcodes import * #dont have to go file.class.attribute

dicts = {} #THEEEE DICTIONARY public

def readCSV(Fname):
    try:
        f = open(Fname, newline='')
    except:
        print("There is no file called "+Fname)

    else:
        #check project to figure out other stuff

        reader = csv.reader(f)

        for row in reader:
            zipcode = int(row[0])
            city = str(row[1])
            state = str(row[2])
            lat = float(row[3])  # longitude
            long = float(row[4])  # latitiude
            TZD = int(row[5])  # time zone difference
            DST = int(row[6])  # daylight savings time
            # #I stored it as an int  instead of a bool to pass the unit test

            dicts[zipcode] = Zipcode(zipcode,Geolocation(lat,long),Location(city,state),TZD,DST)
        f.close()

# daytime.now

def findByState(list):
    states = set()
    for k in dicts.keys():
        for i in range(0,len(list)):
            if dicts[k].location.state == list[i]:
                states.add(dicts[k].zipcode)
    return states

def findByZipcode(zip,x= dicts):
    storage = {}
    for k in x.keys():
        if zip == k:
            objects = x[k]
            storage["zipcode"] = objects.zipcode
            storage["city"] = objects.location.city
            storage["state"] = objects.location.state
            storage["latitude"] = objects.geolocation.latitude
            storage["longitude"] = objects.geolocation.longitude
            storage["timezoneDiff"] = objects.timezonediff
            storage["observeDaylightSavings"] = objects.observeDayLight
    return storage

def findInSameState(list1,list2):
    same = {}
    state = set()

    for i in range(0,len(list1)):
        #state.add(list1[i].location.state)
        for k in range(0,len(list2)):
            if list1[i].location.state == list2[k].location.state:
                state.add(list2[k].location.state)
    for i in list1:
        if i.location.state in state:
            same[i.zipcode] = i
    for i in list2:
        if i.location.state in state:
            same[i.zipcode] = i
    return same

if __name__ == "__main__":
    print("\nLoad the Short List of Zipcodes")
    zipcodeDict = dicts

    #This location will change for each student's code
    readCSV("ShortListZipcodes.csv")
    print("Uniontown Zipcode:\n" + str(zipcodeDict[15401]))

    print("\nTest findByZipcode:\n")
    hburg = findByZipcode(16648)
    print("Hollidaysburg:" + str(hburg))
    assert "Hollidaysburg" == hburg["city"]

    ut = findByZipcode(15401)
    print("Uniontown:" + str(ut))
    assert "PA" == ut["state"]

    sc = findByZipcode(16803)
    print("State College:" + str(sc))
    assert 16803 == sc["zipcode"]

    og = findByZipcode(84201)
    print("Ogden:" + str(og))
    assert -112.007924 == og["longitude"]

    sl = findByZipcode(46982)
    print("Silver Lake:" + str(sl))
    assert 0 == sl["observeDaylightSavings"]

    vegas = findByZipcode(89103)
    print("Las Vegas:" + str(vegas))
    assert 36.113211 == vegas["latitude"]

    ca = findByZipcode(90210)
    print("Beverly Hills:" + str(ca))
    assert -8 == ca["timezoneDiff"]

    print("\nTest findByState:\n")
    zipsByStates = findByState(["NY", "CA", "UT"])
    print(zipsByStates)
    assert 4 == len(zipsByStates)

    print("\nTest findInSameState:\n")
    setA = [zipcodeDict[16648], zipcodeDict[84201], zipcodeDict[15401]]
    setB = [zipcodeDict[16803], zipcodeDict[89101], zipcodeDict[90210]]
    sameState = findInSameState(setA, setB)
    for z in sameState:
        print(z)
    assert 3 == len(sameState)
    assert sameState[16648].location.city in ["Hollidaysburg", "Uniontown", "State College"]
