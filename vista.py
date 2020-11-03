#!/usr/bin/python3
import cgi, cgitb; cgitb.enable()
from string import Template
import xml.etree.cElementTree as ET

def view(mssge):
        print("Content-type: text/html; charset=utf-8\n\n")
        print(" ")
        idpr1,nompro1,prec1 = mssge[0]
        idpr2,nompro2,prec2 = mssge[1]
        idpr3,nompro3,prec3 = mssge[2]
        idpr4,nompro4,prec4 = mssge[3]
        idpr5,nompro5,prec5 = mssge[4]
        idpr6,nompro6,prec6 = mssge[5]
        with open("pagina.html") as template:
                html_template = template.read()

        subst_dict = dict (
                nm1 = nompro1,
                pr1 = prec1,
                nm2 = nompro2,
                pr2 = prec2,
                nm3 = nompro3,
                pr3 = prec3,
                nm4 = nompro4,
                pr4 = prec4,
                nm5 = nompro5,
                pr5 = prec5,
                nm6 = nompro6,
                pr6 = prec6
        )
        print(Template(html_template).safe_substitute(subst_dict))
