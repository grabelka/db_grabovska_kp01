class Validator:

    def __init__(self):  
        print()

    def checkStr(self, val):
        if(not val):
            return False
        val = val.strip()
        if (len(val) < 2) :
            return False
        return True

    def checkNum(self, val):
        try:
            int(val)
        except ValueError:
            return False
        return True