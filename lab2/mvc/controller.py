from model import curators
from model import groups
from model import students
from model import subjects
from view import view

v = view()
c = curators()
g = groups()
st = students()
s = subjects()

com = v.readCommand()
if (com == 'readCuratorGroup'):
    id = v.getNum() 
    code = v.getStr()
    c.readGroup(id, code)
elif(com == 'readCuratorSubject'):
    id = v.getNum() 
    surname = v.getStr()
    c.readSubject(id, surname)
elif (com == 'readStudentCurator'):
    id = v.getNum() 
    surname = v.getStr()
    c.readStudent(id, surname)
elif (com == 'create' or com == 'delete' or com == 'update' or com == 'random'):
    tab = v.readTable()
    if(com == 'random' and tab == 'curators'):
        n = v.getNum()
        c.random(n)
    elif(com == 'delete' and tab == 'curators'):
        id = v.getNum()
        c.delete(id)
    elif(com == 'create' and tab == 'curators'):
        id = v.getNum()
        name = v.getStr()
        surname = v.getStr()
        phone = v.getStr()
        c.create(id, name, surname, phone)
    elif(com == 'update' and tab == 'curators'):
        id = v.getNum()
        name = v.getStr()
        surname = v.getStr()
        phone = v.getStr()
        c.update(id, name, surname, phone)
    elif(com == 'delete' and tab == 'groups'):
        id = v.getNum()
        g.delete(id)
    else:    
        print('Invalid values')
else:    
    print('Invalid values')