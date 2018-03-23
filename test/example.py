# !/usr/bin/python 
# -*- coding: UTF-8 -*-

#############################################################################
# Nombre del programa:  program1_v1.0                                       #    
# Correo Electronico:   afarable-1997@hotmail.com                           #
# Fecha:                08/03/2018                                          #
# Descripción:          Programa encargado de realizar la media aritmetica  #
#                       y la Desviación estandar de 10 numero reales        #
#############################################################################
__author_ = 'Danny Rojas Reyes'
__version__ = 'program1_v1.0.py'

from math import pow, sqrt

""" Descripción de la clase
#Nombre: Operation                                                                                       
#Descripción: se ejecutaran las distintas operaciones para sacar la media y la desviación estándar      
#Constructor: Operation()
#Parámetros del constructor:  null

#Metodos: 4(diferenciaExp, dEstandar, promedioX, promedioX, sumatoria)
"""
class Operation:

    elevar = list()
    def diferenciaExp(self, datos, media):
        for i in datos:
            op = i - media
            self.elevar.append(pow(op, 2))
        return self.dEstandar(sum(self.elevar))
      
    def dEstandar(self, diferencia_elevada):
        
        return round(
            sqrt((diferencia_elevada / (len(self.elevar) - 1))), 3
            )    

    def promedioX(self, data):
        suma = self.sumatoria(data)
        return suma / (len(data))

    def sumatoria(self, datos):
        sumatoria = float(sum(datos))
        return sumatoria


""" Descripción de la clase
#Nombre: inputData                                                                                       
#Descripción: se ejecuta en primera instancia.     
#Constructor: inputData()
#Parámetros del constructor:  null

#Metodos: 1(main)
"""

class inputData:

    def main():
        operations = Operation()
        listaDatos = []
        repetir = int(raw_input('Cuantos valores quieres ingresar? : '))

        for i in range(repetir):
            number = float(raw_input('Escribe el dato: '))
            listaDatos.append(number)

        #Promedio de los datos x.
        media = operations.promedioX(listaDatos)
        print "Media Aritmetica: "  + str(media)
        
        #Desviación Estandar.
        diferenciaExp = operations.diferenciaExp(listaDatos, media)
        print "Desviacion Estandar: " + str(diferenciaExp)
    if __name__ == '__main__':
        main()