class Passport:
    def __init__(self,first_name, last_name, birthday, number, country):
        self.first_name = first_name
        self.last_name = last_name
        self.birthday = birthday
        self.number = number
        self.country = country


    def print_info(self):
        print(self.first_name, self.last_name, self.birthday, self.number, self.birthday)


class ForeignPassport(Passport):
    def __init__(self, first_name, last_name, birthday, number, country, visa):
        self.visa = visa
        super().__init__(first_name, last_name, birthday, number,country)


    def print_info(self):
        super().print_info()
        print(self.visa)


passportlist=[]
foreignpassport=ForeignPassport("David", "Azdza", "12.03.2023", 12345,"Russia", "есть")
passport = Passport("David", "Azdza", "12.03.2023", 22345,"Russia")
passort
