# Napisz program, który tworzy obiekt klasy Person. Klasa posiada
# atrybuty: name, surname, age. Program pozwala na uzupełnienie wartości atrybutów
# danymi podanymi z klawiatury. Wiek musi być liczba całkowita w zakresie od 0 do
# 130, a imie i nazwisko musza posiadać minimum 3 znaki - wykorzystaj w tym celu
# właściwości.
# Klasa Person powinna definiować metode __str__(). Nastepnie,
# zaimplementuj dwie klasy Student i Employee, oparte na klasie Person. W klasie Student
# dodaj atrybuty field_of_study i student_book - słownik, którego klucze to nazwy
# przedmiotów, a wartości to oceny. W klasie Employee dodaj atrybut job_title i skills
# - lista kluczowych umiej etności. Zaimplementuj odpowiednie metody pozwalajace na
# uzupełnianie i wyświetlanie wartości atrybutów w obu klasach potomnych.


class Person:
    def __init__(self, name="brak", surname="brak", age=0):
        self.__name = name
        self.__surname = surname
        self.__age = age

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if len(value) > 3:
            self.__name = value
        else:
            print("Błąd imie musi być dłuższe niż 3 znaki!")

    @property
    def surname(self):
        return self.__surname

    @surname.setter
    def surname(self, value):
        if value.length() > 3:
            self.__surname = value
        else:
            print("Błąd imie musi być dłuższe niż 3 znaki!")

    @property
    def age(self):
       return self.__age

    @age.setter
    def age(self, value):
        if 0 < value < 130:
            self.__surname = value
        else:
            print("Błąd imie musi być dłuższe niż 3 znaki!")

    def __str__(self):
        napis = "Imie: " + self.name + "\nNaziwsko: " + self.surname + "\nWiek: " + str(self.age)
        return napis
#-------------Person-----------------------

print("Tworzenie nowego uzytkownika")
print("Podaj imie")
imie = input()
print("Podaj nazwisko")
nazwisko = input()
print("Podaj wiek")
wiek = input()
wiek = int(wiek)
osoba = Person(imie, nazwisko, wiek)
print(osoba)

