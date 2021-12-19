class View:

    def __init__(self):  
        print('----------Welcome-----------')

    def readCommand(self):
        com = input("Enter a command (read, create, delete, update, random, plot, index, trigger, restore or exit): ")
        return com

    def readTable(self):        
        tab = input("Enter a table name: ")
        if(tab == 'classes' or tab == 'groups' or tab == 'teachers'):
            return tab
        return ''

    def readIndex(self):        
        tab = input("Enter drop or create: ")
        if(tab == 'drop' or tab == 'create'):
            return tab
        return ''
    
    def getName(self):
        val = input("Enter a name: ")
        return val

    def getSurname(self):
        val = input("Enter a surname: ")
        return val
    def getNum(self):
        val = input("Enter a number of random entities: ")
        return int(val)

    def getID(self):
        val = input("Enter an id: ")
        return int(val)

    def getYear(self):
        val = input("Enter a year: ")
        return int(val)

    def getExc(self):
        val = input("Enter a number of excelent students: ")
        return int(val)

    def getTeacher(self):
        val = input("Enter a teacher id: ")
        return int(val)