class NCCAAFootballplayer:
    firstName = ""
    lastname = ""
    year = ""
    position = ""
    unit = ""
    number = 0;

    def __init__(self, _firstName, _lastName, _year, _position, _number):
        self.firstName = _firstName
        self.lastname = _lastName
        fullYearName(_year)
        fullPositionName(_position)
        number = _number

    def fullYearName(self, _year):
        if _year == 'Fr.':
            self.year = 'freshman'
        elif _year == 'So.':
            self.year = 'sophomore'
        elif _year == 'Jr.':
            self.year = 'junior'
        elif _year == 'Sr.':
            self.year = 'senior'
        elif _year == 'R-Fr.':
            self.year = 'redshirt freshman'
        elif _year == 'R-So.':
            self.year = 'resdshirt sophomore'
        elif _year == 'R-Jr.':
            self.year = 'redshirt junior'
        elif _year == 'R-Sr.':
            self.year = 'redshirt senior'
        else:
            self.year = 'INVALID'
    def fullPositionName(self, _position):
        if _position == 'WR':
            self.position = 'wide reciever'
            self.unit = 'o'
        elif _position == 'CB':
            self.position = 'cornerback'
            self.unit = 'd'
        elif _position == 'NB':
            self.position = 'nickelback'
            self.unit = 'd'
        elif _position == 'DB':
            self.position = 'defensive back'
            self.unit = 'd'
        elif _position == 'S':
            self.position = 'safety'
            self.unit = 'd'
        elif _position == 'QB':
            self.position = 'quarterback'
            self.unit = 'o'
        elif _position == 'LB':
            self.position = 'linebacker'
            self.unit = 'd'
        elif _position == 'ILB':
            self.position = 'inside linebacker'
            self.unit = 'd'
        elif _position == 'OLB':
            self.position = 'outside linebacker'
            self.unit = 'd'
        elif _position == 'RB':
            self.position = 'running back'
            self.unit = 'o'
        elif _position == 'TE':
            self.position = 'tight end'
            self.unit = 'o'
        elif _position == 'P/PK':
            self.position = 'punter/placekicker'
            self.unit = 's'
        elif _position == 'P':
            self.position = 'punter'
            self.unit = 's'
        elif _position == 'PK':
            self.position = 'placekicker'
            self.unit = 's'
        elif _position == 'K':
            self.position = 'kicker'
            self.unit = 's'
        elif _position == 'LS':
            self.position = 'long snapper'
            self.unit = 's'
        elif _position == 'DE':
            self.position = 'defensive end'
            self.unit = 'd'
        elif _position == 'DT':
            self.position = 'defensive tackle'
            self.unit = 'd'
        elif _position == 'DL':
            self.position = 'defensive lineman'
            self.unit = 'd'
        elif _position == 'DE/DT':
            self.position = 'defensive end/defensive tackle'
            self.unit = 'd'
        elif _position == 'OLB/DE':
            self.position = 'outside linebacker/defensive end'
            self.unit = 'd'
        elif _position == 'OL':
            self.position = 'offensive lineman'
            self.unit = 'o'
        elif _position == 'G':
            self.position = 'guard'
            self.unit = 'o'
        elif _position == 'NG':
            self.position = 'nose guard'
            self.unit = 'o'
        elif _position == 'NT':
            self.position = 'nose tackle'
            self.unit = 'o'
        else:
            self.position = 'INVALID'
    def generateCode (self, teamCharacter):
        print(teamCharacter + number + unit)

    def generateC1(self, teamName):
        print (teamName +" "+ self.year + " " + self.position + " " + self.firstName + " "+ self.lastname + " (" + self.number + ")")

    def generateC2(self, teamName, teamMascot):
        print (self.firstName + " "+ self.lastname +  " (" + self.number + ")" + " of the " + teamName + teamMascot)

def main():
    tylerHuntley = NCAAFootballplayer("Tyler", "Huntley", "Sr.", "QB", 1)
    tylerHuntley.generateCode('u')
    tylerHuntley.generateC1("University of Utah")
