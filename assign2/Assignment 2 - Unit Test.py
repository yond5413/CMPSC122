if __name__ == "__main__":
    print("\nLoad the Short List of Zipcodes")
    zipcodeDict = dicts

    #This location will change for each student's code
    readCSV("X:\\Downloads\\ShortListZipcodes.csv")
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
