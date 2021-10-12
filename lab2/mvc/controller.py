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
    print() 
elif(com == 'deleteStudentFromGroup'):
    print()
elif (com == 'readStudentCurator'):
    print()
elif (com == 'create' or com == 'delete' or com == 'update' or com == 'random'):
    tab = v.readTable()
    if(com == 'delete' and tab == 'curators'):
        id = v.getId()
        c.delete(id)
    elif(com == 'create' and tab == 'curators'):
        id = v.getId()
        name = v.getVal()
        surname = v.getVal()
        phone = v.getVal()
        c.create(id, name, surname, phone)
    elif(com == 'update' and tab == 'curators'):
        id = v.getId()
        name = v.getVal()
        surname = v.getVal()
        phone = v.getVal()
        c.update(id, name, surname, phone)
    else:    
        print('Invalid values')
else:    
    print('Invalid values')

