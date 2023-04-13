import re

class EmailExtractor:
    def __init__(self, email):
        self.email = email
        self.pattern = r'^(?P<imie>[a-z]+)\.(?P<nazwisko>[a-z]+)([0-9]{2})?@((?P<student>[a-z]+)\.)?wat\.edu\.pl$'

    def parse(self):
        match = re.match(self.pattern, self.email)
        if match:
            self.imie = match.group('imie')
            self.nazwisko = match.group('nazwisko')
            self.student = match.group('student') is not None
        else:
            self.imie = None
            self.nazwisko = None
            self.student = None

    def get_name(self):
        return self.imie.capitalize()

    def get_surname(self):
        return self.nazwisko.capitalize()

    def is_student(self):
        return self.student

    def is_female(self):
        if self.imie and self.imie[-1] == 'a':
            return True
        else:
            return False