# User-Klasse, die eine Erweiterung der Person-Klasse darstellt

from person import Person

class User(Person):
    def __init__(self, first_name, last_name, gender,
                 phone_number, date_of_birth,
                 username, password):
        
        # wende die __init__-Methode der Person-Klasse an:

        Person.__init__(self, first_name, last_name, gender,
                        phone_number, date_of_birth)

        self.username = username
        self.password = password