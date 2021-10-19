class view:

    def __init__(self):  
        print('----------Welcome----------')

    def readCommand(self):
        com = input("Enter command (create, delete, update, random, readCuratorGroup, readCuratorSubject, readStudentCurator): ")
        return com

    def readTable(self):        
        tab = input("Enter table name: ")
        if(tab == 'curators' or tab == 'groups' or tab == 'students' or tab == 'subjects'):
            return tab
        return ''
    
    def getStr(self):
        val = input("Enter a value: ")
        return val

    def getNum(self):
        val = input("Enter a number: ")
        try:
            int(val)
        except ValueError:
            print(val + " is invalid")
            return 0
        return int(val)