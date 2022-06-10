import mysql.connector


def con():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="aroon wanthong",
    )
    return mydb


class Con:
    def getHW():
        mydb = con()

        mycursor = mydb.cursor(dictionary=True)

        sql = "SELECT * FROM hard_ware"

        mycursor.execute(sql)

        data = mycursor.fetchall()

        mycursor.close()

        mydb.close()

        return data

    def getHWByID(ID):
        mydb = con()

        mycursor = mydb.cursor(dictionary=True)

        sql = "SELECT * FROM hard_ware WHERE id = {}".format(ID)

        mycursor.execute(sql)

        data = mycursor.fetchall()

        mycursor.close()

        mydb.close()

        return data

    def getHWByName(name):
        mydb = con()

        mycursor = mydb.cursor(dictionary=True)

        sql = "SELECT * FROM hard_ware WHERE name = '{}'".format(name)

        mycursor.execute(sql)

        data = mycursor.fetchall()

        mycursor.close()

        mydb.close()

        return data

    def addHW(name, hw_name):
        mydb = con()

        mycursor = mydb.cursor(dictionary=True)

        sql = "INSERT INTO hard_ware (name, hw_name, status, value) VALUES ('{}', '{}','OFF',0.00)".format(
            name, hw_name
        )

        mycursor.execute(sql)

        mydb.commit()

        mycursor.close()

        mydb.close()

        ID = mycursor.lastrowid

        return ID

    def updateStatusHW(ID, status):
        mydb = con()

        mycursor = mydb.cursor(dictionary=True)

        sql = "UPDATE hard_ware SET status = '{}' WHERE id = {}".format(status, ID)

        mycursor.execute(sql)

        mydb.commit()

        mycursor.close()

        mydb.close()

        return True

    def updateValueHW(ID, value):
        mydb = con()

        mycursor = mydb.cursor(dictionary=True)

        sql = "UPDATE hard_ware SET value = {} WHERE id = {}".format(value, ID)

        mycursor.execute(sql)

        mydb.commit()

        mycursor.close()

        mydb.close()

        return True

    def DeleteHW(ID):
        mydb = con()

        mycursor = mydb.cursor(dictionary=True)

        sql = "DELETE FROM hard_ware WHERE id = {}".format(ID)

        mycursor.execute(sql)

        mydb.commit()

        mycursor.close()

        mydb.close()

        return True


class Con2:
    def login(user):
        mydb = con()

        mycursor = mydb.cursor(dictionary=True)

        sql = "SELECT * FROM users WHERE username = '{}' and password = '{}'".format(user.username, user.password)

        mycursor.execute(sql)

        data = mycursor.fetchall()

        mycursor.close()

        mydb.close()

        return data
    

    def getUser(ID):
        mydb = con()

        mycursor = mydb.cursor(dictionary=True)

        sql = "SELECT * FROM users WHERE id = {}".format(ID)

        mycursor.execute(sql)

        data = mycursor.fetchall()

        mycursor.close()

        mydb.close()

        return data


    def register(user):
        
        mydb = con()

        mycursor = mydb.cursor(dictionary=True)

        sql = "INSERT INTO users (username, password, name, last_name, address) VALUES ('{}', '{}', '{}', '{}', '{}')".format(user.username, user.password, user.name, user.last_name, user.address)

        mycursor.execute(sql)

        mydb.commit()

        mycursor.close()

        mydb.close()

        ID = mycursor.lastrowid

        return ID

    def checkUserForRegister(username):
        
        mydb = con()

        mycursor = mydb.cursor(dictionary=True)

        sql = "SELECT username FROM users WHERE username = '{}'".format(username)

        mycursor.execute(sql)

        data = mycursor.fetchall()

        mycursor.close()

        mydb.close()

        return data

    
    def changePassword(user):
        mydb = con()

        mycursor = mydb.cursor(dictionary=True)

        sql = "UPDATE users SET password = '{}' WHERE id = {}".format(user.password,user.ID)

        mycursor.execute(sql)

        mydb.commit()

        mycursor.close()

        mydb.close()

        return True
    
    def deleteUser(user):
        mydb = con()

        mycursor = mydb.cursor(dictionary=True)

        sql = "DELETE FROM users WHERE id = {}".format(user.ID)

        mycursor.execute(sql)

        mydb.commit()

        mycursor.close()

        mydb.close()

        return True
    
    def getUser(id):
        mydb = con()
        mycursor = mydb.cursor(dictionary=True)
        sql = "SELECT * FROM users WHERE id = {}".format(id)
        mycursor.execute(sql)
        data = mycursor.fetchall()
        mycursor.close()
        mydb.close()
        return data

    def changePassword_and_Name(users):
        mydb = con()

        mycursor = mydb.cursor(dictionary=True)

        sql = "UPDATE users SET password = '{}', Name= '{}' WHERE id = {}".format(users.password,users.name,users.id)

        mycursor.execute(sql)

        mydb.commit()

        mycursor.close()

        mydb.close()

        return True
    

class Con3():
    def get_hw_ID(id):
        mydb = con()
        mycursor = mydb.cursor(dictionary=True)
        sql = "SELECT * FROM hard_ware WHERE id = {}".format(id)
        mycursor.execute(sql)
        data = mycursor.fetchall()
        mycursor.close()
        mydb.close()
        return data
    
    def updata_hardware(status,value,id):
        mydb = con()
        mycursor = mydb.cursor(dictionary=True)
        sql = "UPDATE hard_ware SET status = '{}' , value= {} WHERE id = {}".format(status,value,id)
        mycursor.execute(sql)
        mydb.commit()
        mycursor.close()
        mydb.close()        
        return True