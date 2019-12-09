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

positionAndUnitDictionary = {
        'WR': ('wide reciever', 'o'),
        'CB': ('cornerback', 'd'),
        'NB': ('nickelback', 'd'),
        'DB': ('defensive back', 'd'),
        'S': ('safety', 'd'),
        'QB': ('quarterback', 'o'),
        'LB': ('linebacker', 'd'),
        'ILB': ('inside linebacker', 'd'),
        'OLB': ('outside linebacker', 'd'),
        'RB': ('running back', 'o'),
        'TE': ('tight end', 'o'),
        'P/PK': ('punter/placekicker','s'),
        'P': ('punter', 's'),
        'PK': ('placekicker', 's'),
        'K': ('kicker', 's'),
        'LS': ('long snapper', 's'),
        'DE': ('defensive end', 'd'),
        'DT': ('defensive tackle', 'd'),
        'DL': ('defensive lineman', 'd'),
        'DE/DT': ('defensive end/defensive tackle', 'd'),
        'OLB/DE': ('outside linebacker/defensive end', 'd'),
        'OL': ('offensive lineman', 'o'),
        'G': ('guard', 'o'),
        'NG': ('nose guard', 'o'),
        'NT': ('nose tackle', 'o'),
        'SN': ('long snapper', 's'),
        'Spec': ('specialist','s')
    }

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
        isPosition = re.search('(^[A-Z]{1,3}$|^P\/PK$|^Spec$|^DT\/DE$|^OLB\/DE$)', element)
        if isPosition and element in positionAndUnitDictionary:
            positionAndUnit = positionAndUnitDictionary[element]
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