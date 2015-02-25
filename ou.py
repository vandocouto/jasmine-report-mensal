#!/usr/bin/python
#-=- encoding: latin-1 -=-


from envia_email import envia_email
from bd_select  import bd_select
from data import data

# Departamento e email do gestor da área.
OU=('TI','email@dominio.com.br')


valor=len(OU)
cont=0
if data()[0] != 0:
    while cont < len(OU):
        if cont % 2 == 0:
            if bd_select(OU[cont]) != 0:
                print OU[cont]
                print OU[cont+1]
                envia_email(OU[cont],OU[cont],OU[cont +1])
        cont +=1







