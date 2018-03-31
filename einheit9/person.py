class Person(object):

    def __init__(self, first_name, last_name, gender,
                 phone_number, date_of_birth):
        # self = das Person-Objekt, das gerade initialisiert wird

        # speichere die uebergebenen daten im Objekt ab:
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.phone_number = phone_number
        self.date_of_birth = date_of_birth
        

    def get_full_name(self):
        # self = das Objekt, dessen Name gerade abgefragt wird
        full_name = self.first_name + ' ' + self.last_name
        return full_name

    def get_age(self):
        year_of_birth = self.date_of_birth[0:4]
        year_of_birth = int(year_of_birth)
        return 2018 - year_of_birth

marko = Person('Marko', 'Knoebl', 'm', '01234', '1988-04-20')

print marko.get_age()

print marko.get_full_name()