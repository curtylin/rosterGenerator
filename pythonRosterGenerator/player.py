import re

class NCCAAFootballplayer:
    firstName = ""
    lastname = ""
    year = ""
    position = ""
    unit = ""
    jerseyNumber = 0
    schoolName = ""
    teamCharacter = ""
    teamMascot = ""

    def __init__(self):
        jerseyNumber = 0

    def generateCode (self):
        return (self.teamCharacter + self.number + self.unit)

    def generateC1(self):
        return (self.schoolName +" "+ self.year + " " + self.position + " " + self.firstName + " "+ self.lastname + " (" + self.number + ")")

    def generateC2(self):
        return (self.firstName + " "+ self.lastname +  " (" + self.number + ")" + " of the " + self.schoolName + " " + self.teamMascot)

    def set_firstName(self, _firstName):
        self.firstName = _firstName

    def set_lastName(self, _lastName):
        self.lastname = _lastName

    def set_YearName(self, _year):
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

    def set_PositionName(self, _position):
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
            self.unit = 'INVALID'

    def set_jerseyNumber(self, _jerseyNumber):
        self.jerseyNumber = _jerseyNumber

    def set_schoolInfo(self, _schoolName, _teamCharacter, _teamMascot):
        self.schoolName = _schoolName
        self.teamCharacter = _teamCharacter
        self.teamMascot = _teamMascot

def main():
    teamName = "University of Utah"
    teanCharacter = 'u'
    teamMascot = "Utes"

    txtfileName = "blahblahblah.txt"
    outputFileName = "blahblahblahProcessed.txt"

    readFile = open(txtfileName, 'r')
    outputFile = open(outputFileName, 'w')

    for line in readFile:
        currentPlayer = NCAAFootballplayer()
        set_schoolInfo(teamName, teamCharacter, teamMascot)
        bool firstNameFound = false
        for element in line.split():
            isJerseyNumber = re.search('\d{1,2}', element)
            if isJerseyNumber:
                set_jerseyNumber(element)
                continue
            isYear = re.search('[A-z]{2}\.{1}', element)
            if isYear:
                set_YearName(element)
                continue
            isPosition = re.search('[A-Z]{2,3}', element)
            if isPosition:
                set_PositionName(element)
            isName = re.search('[A-z]+', element)
            if isName:
                if firstNameFound:
                    set_lastName(element)
                    continue
                else:
                    set_firstName(element)
                    continue

        outputFile.write(currentPlayer.generateCode(teamCharacterForTextFile))
        outputFile.write(currentPlayer.generateC1(teamNameForTextFile))
        outputFile.write(currentPlayer.generateC2(teamName, teamMascot))

    readFile.close()
