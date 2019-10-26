class player:
    firstName = ""
    lastname = ""
    year = ""
    position = ""
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
            self.year = 'invalid'

    def fullPositionName(self, _position):
        if _position == 'WR':
            self.position = 'wide reciever'
        elif _position == 'CB':
            self.position = 'cornerback'
        elif _position == 'NB':
            self.position = 'nickelback'
        elif _position == 'DB':
            self.position = 'defensive back'
        elif _position == 'S':
            self.position = 'safety'
        elif _position == 'QB':
            self.position = 'quarterback'
        elif _position == 'LB':
            self.position = 'linebacker'
        elif _position == 'ILB':
            self.position = 'inside linebacker'
        elif _position == 'OLB':
            self.position = 'outside linebacker'
        elif _position == 'RB':
            self.position = 'running back'
        elif _position == 'TE':
            self.position = 'tight end'
        elif _position == 'P/PK':
            self.position = 'punter/placekicker'
        elif _position == 'P':
            self.position = 'punter'
        elif _position == 'PK':
            self.position = 'placekicker'
        elif _position == 'K':
            self.position = 'kicker'
        elif _position == 'LS':
            self.position = 'long snapper'
        elif _position == 'DE':
            self.position = 'defensive end'
        elif _position == 'DT':
            self.position = 'defensive tackle'
        elif _position == 'DL':
            self.position = 'defensive lineman'
        elif _position == 'DE/DT':
            self.position = 'defensive end/defensive tackle'
        elif _position == 'OLB/DE':
            self.position = 'outside linebacker/defensive end'
        elif _position == 'OL':
            self.position = 'offensive lineman'
        elif _position == 'G':
            self.position = 'guard'
        elif _position == 'NG':
            self.position = 'nose guard'
        elif _position == 'NT':
            self.position = 'nose tackle'
        elif _position == 'PK':
            self.position = 'cornerback'
        elif _position == 'PK':
            self.position = 'cornerback'
        elif _position == 'PK':
            self.position = 'cornerback'
