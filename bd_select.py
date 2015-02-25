#!/usr/bin/python
#-=- encoding: latin-1 -=-

# INSTALE O MODULO python-mysqldb
import MySQLdb
import re
from acesso_bd import acesso_bd
from data import data
from listgroups import listgroups
from mes import mes
import datetime
import datetime as DT


# Recebendo as variaveis de acesso no banco
host        =   acesso_bd()[0]
user        =   acesso_bd()[1]
password    =   acesso_bd()[2]
bd_name     =   acesso_bd()[3]
today       =   DT.date.today()
today       =   today - DT.timedelta(days=1)
mes_anterior = datetime.date.today()
mes_anterior = mes(mes_anterior.month - 1)
# media do custo da folha A4.
mediacf     = 0.03
# media do custo do tonner Lexmark t620.
mediact     = 0.02


# função select 
def bd_select(group):
    group=group
    select = '<html><style>\
    .border {font-family: Arial, Sans-Serif; font-size:12px;}\
    .copy, .copy a {width: 660px; margin:0 auto; color: #DD8888;}\
    .formresult {background-color:#FFFF99;display:block;padding:10px;}\
    .seletor {font-family: Arial, Sans-Serif; font-size:6px;}</style>'

    select +='<table class="border" align="center" valign="top" width="1024">'
    HOST = host
    USER = user
    PASSWORD = password
    db = MySQLdb.connect(HOST, USER, PASSWORD)
    cursor = db.cursor()
    cursor.execute("use %s" %bd_name)
    lista1=[]
    lista2=[]
    cont=0
    total=0
    date=''
    
    select+='<tr>\
    <td align="center" width="100" bgcolor="#EEC900"><font size="2px">Departamento</font></td>\
    <td align="center" width="100" bgcolor="#EEC900"><font size="2px">Usu&aacute;rio</font></td>\
    <td align="center" width="100" bgcolor="#EEC900"><font size="2px">M&ecirc;s</font></td>\
    <td align="center" width="100" bgcolor="#EEC900"><font size="2px">Quant. impressas</font></td>\
    <td align="center" width="100" bgcolor="#EEC900"><font size="2px">Folha R$</font></td>\
    <td align="center" width="100" bgcolor="#EEC900"><font size="2px">Tonner R$</font></td>\
    <td align="center" width="130" bgcolor="#EEC900"><font size="2px">M&eacute;dia Folha + Tonner R$</font></td>\
    </tr>'
    try:
        if data()[0] != 0:    
            for a in listgroups(group):
                sql = ("select user,sum(pages) from jobs_log where user='%s' and date>='%s 00:00:00' and date<='%s 23:59:59'" \
                %(a,data()[0],data()[1]))
                cursor.execute(sql)
                resultado = cursor.fetchone()
                if resultado[0] != None:
                    try:
                        while (resultado):
                            lista1.append(resultado)
                            resultado = cursor.fetchone()
                
                        while cont < len(lista1):
                            if cont % 2 == 0:
                                select+='<tr>\
                                <td align="center" bgcolor="#FFFAFA">%s</td>\
                                <td align="center" bgcolor="#FFFAFA">%s</td>\
                                <td align="center" bgcolor="#FFFAFA">%s</td>\
                                <td align="center" bgcolor="#FFFAFA">%s</td>\
                                <td align="center" bgcolor="#FFFAFA">%s</td>\
                                <td align="center" bgcolor="#FFFAFA">%s</td>\
                                <td align="center" bgcolor="#FFFAFA">%s</td>\
                                </tr>'\
                                %(group,str(lista1[cont][0]),mes_anterior,str(lista1[cont][1]),str((int(lista1[cont][1]) * mediacf)),str((int(lista1[cont][1]) * mediact)),str((int(lista1[cont][1]) * mediacf)+(int(lista1[cont][1]) * mediact)))
                            else:
                                select+='<tr>\
                                <td align="center" bgcolor="#EEE9E9">%s</td>\
                                <td align="center" bgcolor="#EEE9E9">%s</td>\
                                <td align="center" bgcolor="#EEE9E9">%s</td>\
                                <td align="center" bgcolor="#EEE9E9">%s</td>\
                                <td align="center" bgcolor="#EEE9E9">%s</td>\
                                <td align="center" bgcolor="#EEE9E9">%s</td>\
                                <td align="center" bgcolor="#EEE9E9">%s</td>\
                                </tr>'\
                                %(group,str(lista1[cont][0]),mes_anterior,str(lista1[cont][1]),str((int(lista1[cont][1]) * mediacf)),str((int(lista1[cont][1]) * mediact)),str((int(lista1[cont][1]) * mediacf)+(int(lista1[cont][1]) * mediact)))
                    
                            total +=(int(lista1[cont][1]) * mediacf) + (int(lista1[cont][1]) * mediact)
                            cont+=1
                    
                    except:
                        continue
            
            select+='</table>'
            select+='<table class="border" align="center" valign="top" width="1024">'
            select+='<tr>\
            <td align="center" bgcolor="#FFFFFF"><b><font size="3px">M&eacute;dia do custo do departamento: %s R$</font></b></td>\
            </tr>\
            </table>'\
            %("%.2f" % total)
            select+="</table>"
            cursor.close()
            if total != 0:
                return select
            else:
                return 0
    except:
        return "Fora da Data"



 
