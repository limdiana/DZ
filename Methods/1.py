"""
Создайте класс Person у которого будут свойства name и age.
Добавьте метод экземпляра который выводит информацию о человеке.
Создайте метод класса который генерирует новый объект класса
который ставить возраст человека: сегодняшний год - год который передают в метод.
(подсказка: тут можно использовать метод today().year класса date из модуля datetime)
Создайте статический метод который проверяет является ли совершеннолетним человек возраст которого передается в метод.
"""
from datetime import date

class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age


    def ptintname(self):
        print(self.name, self.age)

    @classmethod
    def classmethod(cls, year):
        return Person("Diana", date.today().year - year)

    @staticmethod
    def staticmethod(age):
        if age < 18:
            return "no soversh"
        else:
            return "yes soversh"


diana = (Person.classmethod(2004))
print(diana.name)
print(diana.age)
print(diana.staticmethod(18))