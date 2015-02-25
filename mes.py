#!/usr/bin/python
#-=- encoding: latin-1 -=-

def mes(recebe):
    lista=((0,'NOT'),(1,'Janeiro'),(2,'Fevereiro'),
    (3,'Março'),(4,'Abril'),
    (5,'Maio'),(6,'Junho'),
    (6,'Julho'),(7,'Agosto'),
    (9,'Setembro'),(10,'Novembro'),
    (11,'Novembro'),(12,'Dezembro')
    )
    return lista[recebe][1]