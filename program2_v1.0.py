# !/usr/bin/python 
# -*- coding: UTF-8 -*-

#############################################################################
# Nombre del programa:  program2_v1.0                                       #    
# Correo Electronico:   afarable-1997@hotmail.com                           #
# Fecha:                16/03/2018                                          #
# Descripción:          Programa encargado de realizar la tabla de proxy    #
#                       de un programa.                                     #    
#############################################################################
__author__ = 'Danny Rojas Reyes'
__version__ = 'program2_v1.0.py'

import sys
import itertools
import fileinput
from glob import *

""" Descripción de la clase
#Nombre: Operation                                                                                       
#Descripción: se ejecutaran las distintas operaciones para sacar la media y la desviación estándar      
#Constructor: Operation()
#Parámetros del constructor:  null

#Metodos: 3()
"""
class Operaciones:


    numLineas = 0
    numLineaDeClase = 0
    auxContador = 0
    contadorLineas = 0

    contenedor_clases_metodos = list()
    linea_de_clase = list()
    loc_de_clase = list()
       
    def contar_metodos_de_clase(self, linea):

        if(linea.find('class') == 0):
            self.contenedor_clases_metodos.append(linea)
            if(linea.find('class') == 0 & linea.find(':') == 0):
                self.linea_de_clase.append(self.numLineaDeClase)
   
           
        if(linea.find('def') == 0): 
            self.contenedor_clases_metodos.append(linea)

              
    def total_lineas_de_codigo(self):
        fichero = open('resultado.py')
        for linea in fichero.readlines():
            self.numLineaDeClase+=1
            linea = linea.replace(' ', '')
            if(len(linea.lstrip().rstrip()) > 0):
                if(linea[0] != "#"):
                    if(linea[0] != '"'):
                        self.numLineas+= 1
                        self.contar_metodos_de_clase(linea)
        self.numLineaDeClase = 0
        return str(self.numLineas)
                            
    def locs_de_clase(self):
        for item in range(len(self.linea_de_clase)):
            with open('resultado.py') as dato:
                if(self.auxContador == len(self.linea_de_clase) - 1):
                    opcion = itertools.islice(dato,self.linea_de_clase[self.auxContador], None)
                else:
                    opcion = itertools.islice(dato,self.linea_de_clase[self.auxContador], self.linea_de_clase[self.auxContador + 1] - 1)

                for linea in opcion:
                    linea = linea.replace(' ', '')
                    if(len(linea.lstrip().rstrip()) > 0):
                        if(linea[0] != "#"):
                            if(linea[0] != '"'):
                                if(linea.find('import') != 0):
                                    if(linea.find('from') != 0):
                                        if(linea.find('__author__') != 0):
                                            if(linea.find('__version__') != 0):                        
                                                self.contadorLineas+=1 
            self.loc_de_clase.append(self.contadorLineas)  
            self.contadorLineas = 0
            self.auxContador+=1
        
""" Descripción de la clase
#Nombre: Principal                                                                                       
#Descripción: se ejecutaran en primera instancia para instanciar la clase principal      
#Constructor: Principal()
#Parámetros del constructor:  null

#Metodos: 1()
"""

class Principal:      

    def main():

        operacion = Operaciones()
        contClases = 0;
        contMetodos = 0;
        contadorAuxiliar = 0;

        locs_total = operacion.total_lineas_de_codigo()
        operacion.locs_de_clase()

        for item in operacion.contenedor_clases_metodos:
            if item.find('class') == 0:
                operacion.contenedor_clases_metodos[contadorAuxiliar] = item + str(operacion.loc_de_clase[contClases])
                contClases+=1
            contadorAuxiliar+=1

        contClases = 0
        contadorAuxiliar = 0
   
        for item in operacion.contenedor_clases_metodos:
            if item.find('class') == 0:           
                contClases+=1
                contMetodos = 0
                print "-----------------------------------------------------"
                print item.replace(":", '').replace('class', '').replace('\n', ': ').upper().center(50)
                
            if item.find('def') == 0: 
                contMetodos+=1
                print str(contMetodos) + " - " + item.replace('def', '').replace(':', '') 

            contadorAuxiliar+=1

        print "-----------------------------------------------------"
        print "LOCS del programa: " + str(locs_total)
                        
    if __name__ == '__main__':
        ficheros = (fich for fich in iglob("*.py") if fich <> sys.argv[0])
        file("resultado.py","w").writelines(fileinput.input(ficheros))
        main()