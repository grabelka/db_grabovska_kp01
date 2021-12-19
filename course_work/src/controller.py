import timeit
from model import Classes 
from model import Groups 
from model import Teachers 
from view import View
from plots import Plot
from generator import RandomGroups
from generator import RandomClasses
from generator import RandomTeachers
from optimizer import Index
from reserver import Reserver
from restore import Restore
from validator import Validator
 
view = View()
classes = Classes()
groups = Groups()
teachers = Teachers()
plot = Plot()
randomGroups = RandomGroups()
randomClasses = RandomClasses()
randomTeachers = RandomTeachers()
index = Index()
reserver = Reserver()
restore = Restore()
validator = Validator()

cont = True
while(cont):
    com = view.readCommand()
    if (com == 'exit'):
        cont = False
    elif (com == 'restore'):
        restore.Save()
    elif (com == 'index'):
        com = view.readIndex()
        if (com == 'drop'):
            index.Drop()
        elif (com == 'create'):
            index.Create()
    elif (com == 'read' or com == 'create' or com == 'delete' or com == 'update' or com == 'random' or com == 'plot' or com == 'trigger'):
        tab = view.readTable()
        
        if(com == 'read' and tab == 'groups'):
            n = view.getID()
            if (validator.checkNum(n)):
                groups.read(n)
        elif(com == 'read' and tab == 'teachers'):
            n = view.getID()
            if (validator.checkNum(n)):
                teachers.read(n)
        elif(com == 'read' and tab == 'classes'):
            n = view.getID()
            if (validator.checkNum(n)):
                classes.read(n)

        elif(com == 'random' and tab == 'groups'):
            n = view.getNum()
            if (validator.checkNum(n)):
                randomGroups.random(n)
        elif(com == 'random' and tab == 'teachers'):
            n = view.getNum()
            if (validator.checkNum(n)):
                randomTeachers.random(n)
        elif(com == 'random' and tab == 'classes'):
            n = view.getID()
            if (validator.checkNum(n)):
                randomClasses.random(n)

        elif(com == 'create' and tab == 'groups'):
            id = view.getID()
            name = view.getName()
            year = view.getYear()
            num_of_exc = view.getExc()
            teacher = view.getTeacher()
            if (validator.checkNum(id) and validator.checkStr(name) and validator.checkNum(year) and validator.checkNum(num_of_exc) and validator.checkNum(teacher)):
                groups.create(id, name, year, num_of_exc, teacher)
        elif(com == 'create' and tab == 'teachers'):
            id = view.getID()
            name = view.getName()
            surname = view.getSurname()
            if (validator.checkNum(id) and validator.checkStr(name) and validator.checkStr(surname)):
                teachers.create(id, name, surname)
        elif(com == 'create' and tab == 'classes'):
            id = view.getID()
            name = view.getName()
            teacher = view.getTeacher()
            if (validator.checkNum(id) and validator.checkStr(name) and validator.checkNum(teacher)):
                classes.create(id, name, teacher)

        elif(com == 'update' and tab == 'groups'):
            id = view.getID()
            name = view.getName()
            year = view.getYear()
            num_of_exc = view.getExc()
            teacher = view.getTeacher()
            if (validator.checkNum(id) and validator.checkStr(name) and validator.checkNum(year) and validator.checkNum(num_of_exc) and validator.checkNum(teacher)):
                groups.update(id, name, year, num_of_exc, teacher)
        elif(com == 'update' and tab == 'teachers'):
            id = view.getID()
            name = view.getName()
            surname = view.getSurname()
            if (validator.checkNum(id) and validator.checkStr(name) and validator.checkStr(surname)):
                teachers.update(id, name, surname)
        elif(com == 'update' and tab == 'classes'):
            id = view.getID()
            name = view.getName()
            teacher = view.getTeacher()
            if (validator.checkNum(id) and validator.checkStr(name) and validator.checkNum(teacher)):
                classes.update(id, name, teacher)   

        elif(com == 'delete' and tab == 'groups'):
            n = view.getID()
            if (validator.checkNum(n)):
                groups.delete(n)
        elif(com == 'delete' and tab == 'teachers'):
            n = view.getID()
            if (validator.checkNum(n)):
                teachers.delete(n)
        elif(com == 'delete' and tab == 'classes'):
            n = view.getID()
            if (validator.checkNum(n)):
                classes.delete(n)

        elif(com == 'trigger' and tab == 'groups'):
            reserver.GroupTrigger()
        elif(com == 'trigger' and tab == 'teachers'):
            reserver.TeacherTrigger()
        elif(com == 'trigger' and tab == 'classes'):
            reserver.ClassTrigger()

        elif(com == 'plot' and tab == 'groups'):
            start = timeit.timeit()
            index.Drop()
            groups.read(2648)
            index.Create()
            end = timeit.timeit() + 0.001
            first = end - start 
            print("Time: " + str(first))
            start = timeit.timeit()
            groups.read(2648)
            end = timeit.timeit()
            second = end - start + 0.001
            print("Time: " + str(second))
            plot.Create(first, second, "groups")
        elif(com == 'plot' and tab == 'teachers'):
            start = timeit.timeit()
            index.Drop()
            teachers.read(2648)
            index.Create()
            end = timeit.timeit() + 0.001
            first = end - start 
            print("Time: " + str(first))
            start = timeit.timeit()
            teachers.read(2648)
            end = timeit.timeit()
            second = end - start + 0.001
            print("Time: " + str(second))
            plot.Create(first, second, "teachers")
        elif(com == 'plot' and tab == 'classes'):
            start = timeit.timeit()
            index.Drop()
            classes.read(2648)
            index.Create()
            end = timeit.timeit() + 0.001
            first = end - start 
            print("Time: " + str(first))
            start = timeit.timeit()
            classes.read(2648)
            end = timeit.timeit()
            second = end - start + 0.001
            print("Time: " + str(second))
            plot.Create(first, second, "classes")
        else:
            print('Invalid values')
    else:    
        print('Invalid values')


