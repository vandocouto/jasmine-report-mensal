#!/usr/bin/python
#-=- encoding: latin-1 -=-


import datetime
from datetime import date

def data():
    hj = date.today()

    if hj.day == 01:
        data=datetime.date.today() + datetime.timedelta(-1)
        
        if data.day < 10:
            dia="0%s" %data.day
        else:
            dia="%s" %data.day
        
        if data.month < 10:
            mes="0%s" %data.month
        else:
            mes="%s" %data.month
 
        inicio="%s-%s-01" %(data.year,mes)
        fim="%s-%s-%s" %(data.year,mes,dia)
    else:
        inicio,fim=0,0

    return inicio,fim

