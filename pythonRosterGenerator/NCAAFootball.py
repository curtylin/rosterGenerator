import re

def generateCode (teamCharacter, number, unit):
    return (teamCharacter + str(number) + unit)

def generateC1(schoolName, year, position, firstName, lastName, number):
    return (schoolName +" "+ year + " " + position + " " + firstName + " "+ lastName + " (" + str(number) + ")")

def generateC2(firstName, lastName, number, schoolName, teamMascot):
    return (firstName + " "+ lastName +  " (" + str(number) + ")" + " of the " + schoolName + " " + teamMascot)

yearNameDicionary = {
    'Fr.': 'freshman',
    'FR': 'freshman',
    'So.': 'sophomore',
    'SO': 'sophomore',
    'Jr.': 'junior',
    'JR': 'junior',
    'Sr.': 'senior',
    'SR': 'senior',
    'R-Fr.': 'redshirt freshman',
    'R-So.': 'redshirt sophomore',
    'R-Jr.': 'redshirt junior',
    'R-Sr.': 'redshirt senior'
}

positionAndUnitDictionary ={
    'WR': ('wide receiver', 'o'),
    'Wide Receiver': ('wide receiver', 'o'),
    'CB': ('cornerback', 'd'),
    'Corner Back': ('cornerback', 'd'),
    'NB': ('nickelback', 'd'),
    'NickelBack': ('nickelback', 'd'),
    'DB': ('defensive back', 'd'),
    'Defensive Back': ('defensive back', 'd'),
    'S': ('safety', 'd'),
    'Safety': ('safety', 'd'),
    'QB': ('quarterback', 'o'),
    'QuarterBack': ('quarterback', 'o'),
    'LB': ('linebacker', 'd'),
    'Linebacker': ('linebacker', 'd'),
    'ILB': ('inside linebacker', 'd'),
    'Inside Linebacker': ('inside linebacker', 'd'),
    'OLB': ('outside linebacker', 'd'),
    'Outside Linebacker': ('outside linebacker', 'd'),
    'RB': ('running back', 'o'),
    'Running Back': ('running back', 'o'),
    'TE': ('tight end', 'o'),
    'Tight End': ('tight end', 'o'),
    'P/PK': ('punter/placekicker','s'),
    'Punter/PlaceKicker': ('punter/placekicker','s'),
    'P': ('punter', 's'),
    'Punter': ('punter', 's'),
    'PK': ('placekicker', 's'),
    'Place Kicker': ('placekicker', 's'),
    'K': ('kicker', 's'),
    'Kicker': ('kicker', 's'),
    'LS': ('long snapper', 's'),
    'Long Snapper': ('long snapper', 's'),
    'DE': ('defensive end', 'd'),
    'Defensive End': ('defensive end', 'd'),
    'DT': ('defensive tackle', 'd'),
    'Defensive Tackle': ('defensive tackle', 'd'),
    'DL': ('defensive lineman', 'd'),
    'Defensive Line': ('defensive lineman', 'd'),
    'DE/DT': ('defensive end/defensive tackle', 'd'),
    'Defensive End/Defensive Tackle': ('defensive end/defensive tackle', 'd'),
    'OLB/DE': ('outside linebacker/defensive end', 'd'),
    'Outisde Linebacker/Defensive End': ('outside linebacker/defensive end', 'd'),
    'OL': ('offensive lineman', 'o'),
    'Offensive Line': ('offensive lineman', 'o'),
    'G': ('guard', 'o'),
    'Guard': ('guard', 'o'),
    'NG': ('nose guard', 'o'),
    'Nose Guard': ('nose guard', 'o'),
    'NT': ('nose tackle', 'o'),
    'Nose Tackle': ('nose tackle', 'o'),
    'SN': ('long snapper', 's'),
    'Snapper': ('long snapper', 's'),
    'Spec': ('specialist','s')
}

suffixes = {
    'Jr.': 'Jr.',
    'Sr.': 'Sr.',
    'II': 'II',
    'III': 'III',
    'IV': 'IV',
    'V': 'V',
    'VI': 'VI'
}

schoolName = "University of Oregon"
teamCharacter = 'o'
teamMascot = "ducks"

txtfileName = "Oregon"
outputFileName = txtfileName + "Processed.txt"

readFile = open(txtfileName + ".txt", 'r', encoding='cp1252')
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
        #isYear = re.search('(^[A-z]{2}\.{1}$|^R-[A-z]{2}\.{1}$|[A-Z]{2})', element)
        #if isYear and positionNameSet or element in yearNameDicionary:
        if element in yearNameDicionary and positionNameSet:
            year = yearNameDicionary[element]
            yearNameSet = True
            continue
        #isPosition = re.search('(^[A-Z]{1,3}$|^P\/PK$|^Spec$|^DT\/DE$|^OLB\/DE$)', element)
        #if isPosition and element in positionAndUnitDictionary:
        if element in positionAndUnitDictionary:
            positionAndUnit = positionAndUnitDictionary[element]
            position = positionAndUnit[0]
            unit = positionAndUnit[1]
            positionNameSet = True
            continue
        isLastNameCommaFirstName = re.search('([A-z]+,|([A-z]+.,))', element)
        if isLastNameCommaFirstName:
            lastAndFirstName = element.split(',')
            if lastAndFirstName[0] in suffixes:
                lastName = firstName + lastName + ' ' + lastAndFirstName[0]
                firstNameSet = False
            else:
                lastName = lastName + lastAndFirstName[0]
            lastNameSet = True
            continue
        isName = re.search('([A-z]+)', element)
        if isName:
            if not firstNameSet:
                firstName = element
                firstNameSet = True
                continue
            elif not lastNameSet:
                lastName = lastName + element 
                lastNameSet = True
                continue
            elif element in suffixes:
                lastName = lastName + ' ' + element
                continue
            else:
                print('ERROR ERROR ERROR ERROR')
                continue
                
    code = generateCode(teamCharacter, jerseyNumber, unit)
    c1 = generateC1(schoolName, year, position, firstName, lastName, jerseyNumber)
    c2 = generateC2(firstName, lastName, jerseyNumber, schoolName, teamMascot)
    outputFile.write(code + "\t" + c1 + "\t" + c2 + "\n")
readFile.close()
outputFile.close()