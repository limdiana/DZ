class Work():

    1
    def __init__(self, place):
        self.place = place


    def workinfo(self):
        print("Место работы: ", self.place)


class WorkingStudent(Work):



    def __init__(self, place, name, study):
        super().__init__(place)
        self.name = name
        self.study = study


    def printinfo(self):
        print("Имя: ", self.name)
        print("Место учебы: ", self.study)
        self.workinfo()

Daniil = WorkingStudent("5терочка", "Даня", "Сириус")
Daniil.printinfo()