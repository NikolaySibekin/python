import random

FAMILY = ('Сидоров','Иванов','Петров','Осин','Волин','Сергеев','Дмитриев','Турин','Ткачев','Захаров','Лунев')
NAME = ('Ф.','А.','Д.','С.','Л.','В.','П.','Я.','Н.','Е.')
SUBJECT = ('математика', 'русский язык', 'физика', 'английский язык', 'химия', 'биология')

class School():
    def __init__(self,name):
        self.name = name
        self.Classes = []
    def addClass(self, Clas):
        '''метод добавляет класс в школу'''
        self.Classes.append(Clas)
    def showClasses(self):
        '''метод возвращает все классы в школе'''
        print('Школа {} содержит:'.format(self.name))
        for itm in self.Classes:
            print('класс {}'.format(itm.name))
    def showClass(self, name):
        '''метод возвращает список учеников в классе'''
        for itm in self.Classes:
            if itm.name == name: itm.showClass()
    def showPupilInfo(self, name):
        '''метод возвращает Ученик --> Класс --> Учителя --> Предметы'''
        for cl in self.Classes:
            for pup in cl.Pupils:
                if pup.name == name:
                    for teach in cl.Teachers:
                        print('Ученик {} класс {} преподаватель {} предмет {}'.format(pup.name, cl.name, teach.name, teach.subject))
    def showPupilParents(self, name):
        '''метод возвращающий родителей ученика'''
        for cl in self.Classes:
            for pup in cl.Pupils:
                if pup.name == name: pup.showParents()
    def genSchool(self, classes, pupils, subjects):
        '''метод генерации школы с количеством классов, учеников в классе и количеством предметов в классе'''
        for idx in range(int(classes)):                 
            xclass = Class(str(random.randint(1,11))+random.choice(('A', 'B', 'C', 'D')))
            self.addClass(xclass)
            for i in range(int(pupils)):
                xclass.addPupil(Pupil(random.choice(FAMILY)+' '+random.choice(NAME)+random.choice(NAME),
                                      random.choice(FAMILY)+' '+random.choice(NAME)+random.choice(NAME),
                                      random.choice(FAMILY)+'а '+random.choice(NAME)+random.choice(NAME)))
            for i in range(int(subjects)):
                xclass.addTeacher(random.choice(FAMILY)+random.choice(NAME)+random.choice(NAME), random.choice(SUBJECT))
            
class Class():
    def __init__(self, name):
        self.name = name
        self.Pupils = []
        self.Teachers = []
    def addPupil(self, pupil):
        '''метод добавляет ученика в класс'''
        self.Pupils.append(pupil)
    def addTeacher(self, name, subject):
        '''метод добавляет учителя с предметом в класс'''
        self.Teachers.append(Teacher(name, subject))
    def showClass(self):
        '''метод возвращает список учеников в классе'''
        print('Класс {} содержит:'.format(self.name))
        for itm in self.Pupils:
            print('ученик {}'.format(itm.name))

class Pupil():
    def __init__(self, name, father, mother):
        self.name = name
        self.father = father
        self.mother = mother
    def showParents(self):
        '''метод вовращает родителей ученика'''
        print('Отец - {}, Мать - {}'.format(self.father, self.mother))

class Teacher():
    def __init__(self, name, subject):
        self.name = name
        self.subject = subject