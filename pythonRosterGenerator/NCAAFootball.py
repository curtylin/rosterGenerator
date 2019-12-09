import re

def generateCode (teamCharacter, number, unit):
    return (teamCharacter + str(number) + unit)

def generateC1(schoolName, year, position, firstName, lastName, number):
    return (schoolName +" "+ year + " " + position + " " + firstName + " "+ lastName + " (" + str(number) + ")")

def generateC2(firstName, lastName, number, schoolName, teamMascot):
    return (firstName + " "+ lastName +  " (" + str(number) + ")" + " of the " + schoolName + " " + teamMascot)

def get_YearName(_year):
    if _year == 'Fr.':
        return ('freshman')
    elif _year == 'So.':
        return ('sophomore')
    elif _year == 'Jr.':
        return ('junior')
    elif _year == 'Sr.':
        return ('senior')
    elif _year == 'R-Fr.':
        return ('redshirt freshman')
    elif _year == 'R-So.':
        return ('resdshirt sophomore')
    elif _year == 'R-Jr.':
        return ('redshirt junior')
    elif _year == 'R-Sr.':
        return ('redshirt senior')
    else:
        return ('INVALID')

def get_PositionNameAndUnit(_position):
    if _position == 'WR':
        return ('wide reciever', 'o')
    elif _position == 'CB':
        return ('cornerback', 'd')
    elif _position == 'NB':
        return ('nickelback', 'd')
    elif _position == 'DB':
        return('defensive back', 'd')
    elif _position == 'S':
        return ('safety', 'd')
    elif _position == 'QB':
        return ('quarterback', 'o')
    elif _position == 'LB':
        return ('linebacker', 'd')
    elif _position == 'ILB':
        return ('inside linebacker', 'd')
    elif _position == 'OLB':
        return ('outside linebacker', 'd')
    elif _position == 'RB':
        return ('running back', 'o')
    elif _position == 'TE':
        return ('tight end', 'o')
    elif _position == 'P/PK':
        return ('punter/placekicker','s')
    elif _position == 'P':
        return ('punter', 's')
    elif _position == 'PK':
        return ('placekicker', 's')
    elif _position == 'K':
        return ('kicker', 's')
    elif _position == 'LS':
        return ('long snapper', 's')
    elif _position == 'DE':
        return ('defensive end', 'd')
    elif _position == 'DT':
        return ('defensive tackle', 'd')
    elif _position == 'DL':
        return 'defensive lineman', 'd'
    elif _position == 'DE/DT':
        return ('defensive end/defensive tackle', 'd')
    elif _position == 'OLB/DE':
        return ('outside linebacker/defensive end', 'd')
    elif _position == 'OL':
        return ('offensive lineman', 'o')
    elif _position == 'G':
        return ('guard', 'o')
    elif _position == 'NG':
        return ('nose guard', 'o')
    elif _position == 'NT':
        return ('nose tackle', 'o')
    elif _position == 'SN':
        return ('long snapper', 's')
    elif _position == 'Spec':
        return ('punter/placekicker','s')
    else:
        return ('INVALID', 'INVALID')

schoolName = "University of Utah"
teamCharacter = 'u'
teamMascot = "Utes"

txtfileName = "utahUnedited.txt"
outputFileName = "utahProcessed.txt"

readFile = open(txtfileName, 'r', encoding='cp1252')
outputFile = open(outputFileName, 'w')

for line in readFile:
    firstNameSet = False
    lastNameSet = False
    jerseyNumberSet = False
    yearNameSet = False
    positionNameSet = False
    firstName = ""
    lastName = ""
    jerseyNumber = 0
    year = ""
    position = ""
    unit = ""
    for element in line.split():
        if firstNameSet and lastNameSet and jerseyNumberSet and jerseyNumberSet and yearNameSet and positionNameSet:
            break
        isJerseyNumber = re.search('^\d{1,2}$', element)
        if isJerseyNumber:
            jerseyNumber = int(element)
            jerseyNumberSet = True
            continue
        isYear = re.search('(^[A-z]{2}\.{1}$|^R-[A-z]{2}\.{1}$)', element)
        if isYear:
            year = get_YearName(element)
            yearNameSet = True
            continue
        isPosition = re.search('(^[A-Z]{1,3}$)', element)
        if isPosition:
            positionAndUnit = get_PositionNameAndUnit(element)
            position = positionAndUnit[0]
            unit = positionAndUnit[1]
            positionNameSet = True
            continue
        isName = re.search('[A-z]+', element)
        if isName:
            if firstNameSet:
                lastName = element
                lastNameSet = True
                continue
            else:
                firstName = element
                firstNameSet = True
                continue
    code = generateCode(teamCharacter, jerseyNumber, unit)
    c1 = generateC1(schoolName, year, position, firstName, lastName, jerseyNumber)
    c2 = generateC2(firstName, lastName, jerseyNumber, schoolName, teamMascot)
    outputFile.write(code + "\t" + c1 + "\t" + c2 + "\n")
readFile.close()
outputFile.close()