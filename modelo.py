#!/usr/bin/python3

import mysql.connector
from mysql.connector import errorcode

class Usuario(object):

       def __init__(self, nombre_user, psswd_user):
           self.nombre_usr = nombre_user
           self.psswd_usr = psswd_user

       def name(self):
           return ("%s %s" % (self.nombre_usr, self.psswd_usr))

       @classmethod
       def getUsr(self, nombre, cont):
           #person = Usuario(user_nm, psswd)
           try:
               cnx = mysql.connector.connect(user='Juan-fet', password='password2', database='db3', host='127.0.0.1')
               cursordb = cnx.cursor()
               sql = "SELECT * FROM productos"
               #val = (person.nombre_usr, person.psswd_usr)
               cursordb.execute(sql)
               ans = cursordb.fetchall()
               #if ans == None:
               #    msg1 = "NO esta registrado"
               #    return msg1
               #else:
               #    cursordb.execute("SELECT * FROM user")
               #    msg2 = cursordb.fetchall()
               #    return msg2
               cursordb.close()
               cnx.close()
               return ans
           except mysql.connector.Error as err:
               if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                   eraux1 = ("Something is wrong with your user name or password")
                   return eraux1
               elif err.errno == errorcode.ER_BAD_DB_ERROR:
                   eraux2 = ("Database does not exist")
                   return eraux2
               else:
                   araux3 = (err)
                   return araux3


       @classmethod
       def setUsr(self, user_nm, passwd):
           person = Usuario(user_nm, passwd)
           try:
               cnx = mysql.connector.connect(user='Juan-fet', password='password2', database='db2', host='127.0.0.1')
               cursordb = cnx.cursor()
               sql = "INSERT INTO user(username, password) VALUES (%s, sha(%s))"
               val = (person.nombre_usr, person.psswd_usr)
               cursordb.execute(sql, val)
               cnx.commit()
               aux1 = ("Registro exitoso")
               cursordb.close()
               cnx.close()
               aux2 = ("terminado!")
               return aux1+aux2
           except mysql.connector.Error as err:
               if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                   eraux1 = ("Something is wrong with your user name or password")
                   return eraux1
               elif err.errno == errorcode.ER_BAD_DB_ERROR:
                   eraux2 = ("Database does not exist")
                   return eraux2
               else:
                   araux3 = (err)
                   return araux3
