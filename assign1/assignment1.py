import random
class Player:


    def __init__(self, team, name,height,weight,age,equipment):
        self.team = team
        self.name = name
        self.height = height
        self.weight = weight
        self.age = age
        self.equipment = equipment



    def __str__(self):
        return ("{}\t{}\t{}\t{}\t{}".format(self.team, self.name, self.height,
                self.weight, str(self.equipment))    )



class Jersey:
     sizes = ["XS","S","M","L","XL","XXL"]
     size = 0 # index for sizes list
     def __init__(self,number, colors, size, logo, jersey_name):
        self.number = number
        self.colors = colors
        self.size = size
        self.logo = logo
        self.jersey_name = jersey_name

     def __str__(self):
        return ("{}\t{}\t{}\t{}\t{}".format(self.number,self.colors, self.size,
                self.logo, self.jersey_name))




class Equipment:
    numBalls = 0
    shinguard = ''
    cleats = ''

    def __init__(self, jersey ,numBalls, shinguard, cleats):
        self.jersey = jersey # object
        self.numBalls = numBalls
        self.shinguard = shinguard
        self.cleats = cleats


    def __str__(self):
        return ("{}\t{}\t{}\t{}".format(str(self.jersey), self.numBalls, self.shinguard,
                self.cleats))

class Position:
    position = ""
    def __init__(self,position,player):
        self.position = position
        self.player = player

    def __str__(self):
        return ("{}\t{}".format(self.position, str(self.player)))

class Stat:
    goals = 0
    assists = 0
    yellowCards = 0
    redCards = 0

    def __init__(self,goals,assists, yellowCards,redCards,position):
        self.goals = goals
        self.assists = assists
        self.yellowCards = yellowCards
        self.redCards = redCards

        self.position = position
    def __str__(self):
        return ("{}\t{}\t{}\t{}\t{}".format(self.goals,self.assists,self.yellowCards,self.redCards,self.position))



playerAssociation = []


def addPlayer():

    colors = []
    number = int(input("enter a number for the jersey(integer): "))
    jersey_name = input("Enter the name on the back of the jersey: ")
    logo = str(input("Enter the team badge shape: "))
    size = int(input("Enter the size of the jersey: {0 = XS, 1 = S, 2 = M, 3 = L, 4 = XL, 5 = XXL: ") )



    choice = True

    while choice == True:
        colors.append(str(input("Enter a color")))
        x = int(input("Do you want to add another color? (yes = 1, No = 0)"))
        if x == 1:
            choice = True
        elif x == 0:
            choice = False
        else:
            x = int(input("Do you want to add another color? (yes = 1, No = 0)"))



    Player.name = input("Enter the player's name")  # type: string



    jersey1  = Jersey(number,colors,Jersey.sizes[size],logo,jersey_name)
    Numballs = int(input("Enter the number of balls the needed: "))
    shinGuard = input("Enter the brand of shin guard")
    cleats = input("Enter the brand of cleats")

    equip1 = Equipment(jersey1,Numballs,shinGuard,cleats)

    team = input("Enter the team the player is on")
    name = input("Enter the name of the player")
    height = int(input("Enter the height of the player in inches"))
    weight = int(input("Enter the weight of the player: "))
    age = int(input("Enter the player's age: "))
    player1 = Player(team,name,height,weight,age,equip1)

    return player1




def editPlayer(list = playerAssociation): # only ten changes needed
    for i in range(len(list)):
        print(str(i+1)+"\t"+ str(list[i].name))
    choice = int(input("Enter the player you want to edit.(Enter number beside it): "))
    guy = choice - 1
    p = list[guy]
    change = int(input("Enter what needs to be changed.[1.team 2.name 3. height 4. weight 5. age 6. number 7. color 8. size 9. shinguard 10. cleats:  "))

    if change == 1:
        del list[choice].team
        new_team = input("Enter the player's team: ")
        list[choice].team = new_team
        '''print(list[choice].team)'''# practice run
    elif change == 2:
        del list[choice].name
        new_name = input("Enter the player's name: ")
        list[choice].name = new_name
        #print(list[choice].name)
    elif change == 3:
        del list[choice].height
        new_height = int(input("Enter the player's height:  "))
        list[choice].height = new_height
        #print(list[choice].height)
    elif change == 4:
        del list[choice].weight
        new_weight = int(input("Enter the player's weight:  "))
        list[choice].weight = new_weight
        #print(list[choice].weight)
    elif change == 5:
        del list[choice].age
        new_age = int(input("Enter the player's age:  "))
        list[choice].age = new_age
        #print(list[choice].age)
    elif change == 6:
        del list[choice].equipment.jersey.number
        new_num = int(input("Enter the player's jersey number:   "))
        list[choice].equipment.jersey.number = new_num
        #print(list[choice].equipment.jersey.number)
    elif change == 7:
        del list[choice].equipment.jersey.colors
        new_colors = []
        x = 0
        other = True
        while other == True:
            new_colors.append(str(input("Enter a color:  ")))
            x = int(input("Do you want to add another color? (yes = 1, No = 0):  "))
            if x == 1:
                other = True
            elif x == 0:
                other = False
            else:
                x = int(input("Do you want to add another color? (yes = 1, No = 0):  "))
        list[choice].equipment.jersey.colors = new_colors
        #print(list[choice].equipment.jersey.colors)
    elif change == 8:
        del list[choice].equipment.jersey.size
        for i in range(len(Jersey.sizes)):
            print(str(i + 1) +"\t"+ str(Jersey.sizes[i]))
        x = int(input("Enter the player's jersey size (Number next to size):  "))
        list[choice].equipment.jersey.size = Jersey.sizes[x-1]
        #print(list[choice].equipment.jersey.size)
    elif change == 9:
        del list[choice].equipment.shinguard
        new_shingard = input("Enter the player's shinguard brand:  ")
        list[choice].equipment.shinguard = new_shingard
        #print(list[choice].equipment.shinguard)
    elif change == 10:
        del list[choice].equipment.cleats
        new_cleats = input("Enter the player's brand of cleats:  ")
        list[choice].equipment.cleats = new_cleats
        #print(list[choice].equipment.cleats)


    return list



def printPlayers(list = playerAssociation):
    i = 0
    for i in range(len(list)):
        print(list[i])


def findByJerseyNumber(num ,list = playerAssociation):
    x = []
    for i in list:
        if num == i.equipment.jersey.number:
            x.append(i)
    return x



def findByTeam(team,list = playerAssociation):
    x = []
    for i in list:
        if team == i.team:
            x.append(i)
    return x

#other functions for 2 classes

def addPosition(list = playerAssociation):
    for i in range(len(list)):
        print(str(i+1)+"\t"+ str(list[i].name))
    choice = int(input("Enter the player you want to edit.(Enter number beside it): "))
    who = int(input("Enter the position of the player [1. GK 2. Defence. 3. Midfield 4. Attacker")) # prompts user to enter player position
    if who == 1:
        position = Position("GK", list[choice-1].name)
    elif who ==2:
        position = Position("Defence",list[choice-1].name)
    elif who ==3:
        position = Position("Midfield",list[choice-1].name)
    elif who ==4:
        position = Position("Attacker",list[choice-1].name)
    else:
        choice = int(input("Enter the player you want to edit.(Enter number beside it): "))
        who = int(input( "Enter the position of the player [1. GK 2. Defence. 3. Midfield 4. Attacker"))  # prompts user to enter player position
    return position

def PlayerStats(position,list = playerAssociation):
    for i in range(len(list)):
        print(str(i+1)+"\t"+ str(list[i].name))
    choice = int(input("Enter the player you want to edit.(Enter number beside it): "))
    if Position.position == "GK" and Position.player == list[choice-1].name:
        goals = 0
        assists = 0
        yellows = int(random(0,10))
        reds = int(random(0,8))
        stats = Stat(goals,assists,yellows,reds,Position.position)

    elif Position.position == "Defence" and Position.player == list[choice-1].name:
        goals = int(random(0,8))
        assists = int(random(0,5))
        yellows =  int(random(0,10))
        reds = int(random(0,10))
        stats = Stat(goals,assists,yellows,reds,Position.position)

    elif Position.position == "Midfield" and Position.player == list[choice-1].name:
        goals = int(random(0,20))
        assists = int(random(0,18))
        yellows = int(random(0,8))
        reds = int(random(0,6))
        stats = Stat(goals,assists,yellows,reds,Position.position)
    elif Position.position == "Attacker" :
        goals = int(random(0,49))
        assists = int(random(0,25))
        yellows = int(random(0.5))
        reds = int(random(0,3))
        stats = Stat(goals,assists,yellows,reds,Position.position)
        print(Stat.goals,Stat.assists,Stat.yellowCards, Stat.redCards, Stat.position)






if __name__ == "__main__":
    # Soccer Unit Test
    print("Starting Soccer Unit Test...")
    assert len(playerAssociation) == 0
    print("List size is 0")
    jersey1 = Jersey(10, ["blue", "red", "yellow"], Jersey.sizes[1],
                     "Crest", "Messi")
    equip1 = Equipment(jersey1, 10, "Nike", "Nike")
    messi = Player("Futbol Club Barcelona", "Lionel Messi", 67, 158, 31,
                   equip1)
    playerAssociation.append(messi)
    printPlayers()
    found = findByJerseyNumber(10)
    assert len(found) == 1
    assert found[0].age == 31
    assert found[0].equipment.cleats == "Nike"
    assert found[0].equipment.jersey.number == 10
    print("Found the correct Player: ", found[0].name)

    jersey2 = Jersey(5, ["blue", "red", "yellow"], Jersey.sizes[2], "Crest",
                     "Busquets")
    equip2 = Equipment(jersey2, 5, "Nike", "Nike")
    busquets = Player("Futbol Club Barcelona", "Sergio Busquets", 74, 167,
                      30, equip2)
    playerAssociation.append(busquets)
    assert len(playerAssociation) == 2
    print("List size is 2")
    printPlayers()
    found = findByJerseyNumber(5)
    assert len(found) == 1
    assert found[0].height == 74
    assert "yellow" in found[0].equipment.jersey.colors
    assert "yellow" in found[0].equipment.jersey.colors

    jersey3 = Jersey(15, ["Red", "White", "Black"], Jersey.sizes[3],
                 "Crest", "Ramos")
    equip3 = Equipment(jersey3, 5, "Nike", "Nike")
    ramos = Player("Real Madrid Club de Futbol", "Sergio Ramos", 72, 180,
               32, equip3)
    playerAssociation.append(ramos)
    assert len(playerAssociation) == 3
    print("List size is 2")
    printPlayers()
    assert len(findByTeam("Futbol Club Barcelona")) == 2
    print("Soccer Test Complete")

#editPlayer() '''this works'''
#p = addPosition()  #'''COuldnt get these too work (Uses other two made up classes)'''
#PlayerStats(p)
#^ practice run
