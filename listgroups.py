#!/usr/bin/python
#-=- encoding: latin-1 -=-

import os, commands



def listgroups(group):
    group=group
    user='rootsamba'
    password='senha-do-rootsamba'
    host='192.168.1.41'
    comando=(commands.getoutput("ldapsearch -x -b 'ou=%s,ou=TGL,ou=MATRIZ1,dc=tgl,dc=intranet' \
    -D 'cn=%s,cn=Users,dc=tgl,dc=intranet' -w '%s' -h %s | \
    grep sAMAccountName | awk '{print $2}' | sort" %(group,user,password,host)))
    
    comando = comando.split()
    return comando
