#!/usr/bin/python3

from model import Usuario
import vista
import cgi

def createUsr(cont,usuar):
       advice = Usuario.setUsr(usuar,cont)
       return advice

def consultDB(cont, usuar):
       request = Usuario.getUsr(usuar,cont)
       return request

def start():
        datos = cgi.FieldStorage()
        #passw = format(datos.getvalue('pwd'))
        #usern = format(datos.getvalue('email'))
        mssg = consultDB("juan","1234")
        vista.view(mssg)
if __name__ == "__main__":
       start()
