# danymi podanymi z klawiatury. Wiek musi być liczba całkowita w zakresie od 0 do
# 130, a imie i nazwisko musza posiadać minimum 3 znaki - wykorzystaj w tym celu właściwości.
# Klasa Person powinna definiować metode __str__(). Nastepnie,
# zaimplementuj dwie klasy Student i Employee, oparte na klasie Person. W klasie Student
# dodaj atrybuty field_of_study i student_book - słownik, którego klucze to nazwy
# przedmiotów, a wartości to oceny.
# W klasie Employee dodaj atrybut job_title i skills
# - lista kluczowych umiej etności. Zaimplementuj odpowiednie metody pozwalajace na
# uzupełnianie i wyświetlanie wartości atrybutów w obu klasach potomnych.


class Person:
    def __init__(self, name="null", surname="null", age=0):
        self.__name = name
        self.__surname = surname
        self.__age = age

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        try:
            if len(name) > 3:
                self.__name = name
            else:
                print("Błąd imie musi być dłuższe niż 3 znaki!")
        except ValueError:
            print(f'Fck')

    @property
    def surname(self):
        return self.__surname

    @surname.setter
    def surname(self, surname):
        if len(surname) > 3:
            self.__surname = surname
        else:
            print("Błąd nazwisko musi być dłuższe niż 3 znaki!")
            exit(1)

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        age = int(age)
        if 0 < age < 130:
            self.__age = age
    def __str__(self):
        napis = "Imie: " + self.name + "\nNaziwsko: " + self.surname + "\nWiek: " + str(self.age)
        return napis


class Student(Person):

    def __init__(self, name, surname, age):
        super().__init__(name, surname, age)
        print("Podaj kierunek")
        field_of_study = input()
        self.__field_of_study = field_of_study
        self.__student_book = {}

    @property
    def field_of_study(self):
        return self.__field_of_study

    @field_of_study.setter
    def field_of_study(self, field_of_study):
        self.__field_of_study = field_of_study

    @property
    def student_book(self):
        return self.__student_book

    @student_book.setter
    def student_book(self, value):
        key, mark = value
        if key in self.__student_book.keys():
            self.__student_book[key].append(mark)
        else:
            self.__student_book[key] = mark.split(',')

    def __str__(self):
        napis = "Imie: " + self.name + "\nNaziwsko: " + self.surname + "\nWiek: " + str(self.age) + "\nKierunek: " + \
                self.field_of_study
        return napis


class Employee(Person):

    def __init__(self, name, surname, age):
        super().__init__(name, surname, age)
        print("Podaj zawód")
        job_title = input()
        self.job_title = job_title
        self.skills = []

    @property
    def job_title(self):
        return self.__job_title

    @job_title.setter
    def job_title(self, job_title):
        if len(job_title) >= 3:
            self.__job_title = job_title
        else:
            print("Błąd danych!")

    @property
    def skills(self):
        return self.__skills

    @skills.setter
    def skills(self, value):
        if len(value) >= 3:
            self.__skills = value.split(',')

    def __str__(self):
        return f"Pracownik:\nImię: {self.name}\nNazwisko: {self.surname}\nWiek: {self.age}\n" \
            f" Stanowisko: {self.job_title}"


print("Kogo utworzyc?")
print("1 - Osoba\n2 - Student\n3 - Pracownik\n9 - EXIT")
wybor = input()
wybor = int(wybor)
# -------------------Person----------------------------
if wybor == 1:
    print("Prosze podać imię: ")
    imie = input()
    print("Prosze podać nazwisko: ")
    nazwisko = input()
    print("Prosze podać wiek: ")
    wiek = input()
    wiek = int(wiek)
    osoba = Person(imie, nazwisko, wiek)
    print(osoba)
# -----------------Student----------------------------
elif wybor == 2:
    print("Prosze podać imię studenta: ")
    imie = input()
    print("Prosze podać nazwisko studenta: ")
    nazwisko = input()
    print("Prosze podać wiek studenta: ")
    wiek = input()
    wiek = int(wiek)
    student = Student(imie, nazwisko, wiek)
    print(student)
    k = 0
    while k != 'y':
        print('Przedmiot:')
        z = input()
        print('Oceny (odziel oceny przecinkiem):')
        y = input()
        student.student_book = (z, y)
        print("Zakończ y/n")
        k = input()
    for k, v in student.student_book.items():
        print(k, v)
# -----------------Employee----------------------------
elif wybor == 3:
    print("Prosze podać imię pracownika: ")
    imie = input()
    print("Prosze podać nazwisko pracownika: ")
    nazwisko = input()
    print("Prosze podać wiek pracownika: ")
    wiek = input()
    wiek = int(wiek)
    pracownik = Employee(imie, nazwisko, wiek)
    print(pracownik)
    k = 0
    while k != 'y':
        print('Umiejetnosci: (oddziel przecinkiem)')
        z = input()
        pracownik.skills = z
        print("Zakończ y/n")
        k = input()
    for s in pracownik.skills:
        print(s)

# -----------------EXIT----------------------------
elif wybor == 9:
    exit(1)
