class view:

    def __init__(self):  
        print('----------Welcome----------')

    def readCommand():
        com = input("Enter command (create, delete, update, random, readCuratorGroup, deleteStudentFromGroup, readStudentCurator): ")
        return com

    def readTable():        
        tab = input("Enter table name: ")
        if(tab == 'curators' or tab == 'groups' or tab == 'students' or tab == 'subjects'):
            return tab
        return ''
    
    def getVal():
        val = input("Enter value: ")
        return val

    def getId():
        val = input("Enter id: ")
        try:
            int(val)
        except ValueError:
            print(val + " is invalid")
            return 0
        return int(val)
