from xmlrpc.client import boolean
from conDB import Con, Con2, Con3 


class Action:
    def getHW():
        data = Con.getHW()
        return data

    def getHWByID(ID):
        data = Con.getHWByID(ID)
        return data

    def getHWByName(name):
        data = Con.getHWByName(name)
        return data

    def addHW(name, hw_name):
        ID = Con.addHW(name, hw_name)
        data = Con.getHWByID(ID)
        return data

    def updateStatusHW(ID, status):
        boolean = Con.updateStatusHW(ID, status)
        if boolean:
            data = Con.getHWByID(ID)
        else:
            data = {"error": True}
        return data

    def updateValueHW(ID, value):
        boolean = Con.updateValueHW(ID, value)
        if boolean:
            data = Con.getHWByID(ID)
        else:
            data = {"error": True}
        return data

    def DeleteHW(ID):
        boolean = Con.DeleteHW(ID)
        if boolean:
            data = {"error": False, "Delete": "Succeses"}
        else:
            data = {"error": True}
        return data

    def login(user):
        user = Con2.login(user)
        if user:
            data = {"error": False, "user": user}
            return data
        else:
            data = {"error": True}
            return data

    def register(user):
        checkUser = Con2.checkUserForRegister(user.username)
        if(not checkUser):
            ID = Con2.register(user)
            data = Con2.getUser(ID)
            return data
        else:
            data = {"error": True, "username": "error"}
            return data

    def changePassword(user):
        boolean = Con2.changePassword(user)
        if(boolean):
            data = Con2.getUser(user.ID)
            return data
        else:
            data = {"error": True,}
            return data

    def deleteUser(user):
        boolean = Con2.deleteUser(user)
        if(boolean):
            data = {"error": False,}
            return data
        else:
            data = {"error": True,}
            return data
        
    def get_hw_ID(id):
        data = Con3.get_hw_ID(id)
        return data

    def updata_hardware(status,value,id):
        boolean = Con3.updata_hardware(status,value,id)
        if(boolean):
            data = Con3.get_hw_ID(id)
        else:
            data = {"error":True}
        return data
    
    def changePasswordAndName(users):
        boolean = Con2.changePassword_and_Name(users)
        if(boolean):
            data = Con2.getUser(users.id)
            return data
        else:
            data = {"error": True,}
            return data