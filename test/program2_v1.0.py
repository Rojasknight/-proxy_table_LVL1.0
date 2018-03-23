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


""" Descripción de la clase
#Nombre: Operation                                                                                       
#Descripción: se ejecutaran las distintas operaciones para sacar la media y la desviación estándar      
#Constructor: Operation()
#Parámetros del constructor:  null

#Metodos: 4()
"""

import glob
import itertools





class Operaciones:

    seleccion_lenguaje = {"python" : "*.py"}
    numLineas = 0
    numLineaDeClase = 0
    auxContador = 0
    contadorLineas = 0

 
    nombres_clases = list()
    contenedor_clases_metodos = list()

    linea_de_clase = list()
    loc_de_clase = list()
 

    def listar_ficheros(self, lenguaje):
        return glob.glob(self.seleccion_lenguaje[lenguaje])
       
    def contar_metodos_de_clase(self, linea):

        if(linea.find('class') == 0):
            self.contenedor_clases_metodos.append(linea)
            if(linea.find('class') == 0 & linea.find(':') == 0):
                self.linea_de_clase.append(self.numLineaDeClase)
   
           
        if(linea.find('def') == 0): 
            self.contenedor_clases_metodos.append(linea)

              
    def total_lineas_de_codigo(self):

        listaFicheros = self.listar_ficheros("python")

        for fichero in listaFicheros:
            if(fichero != __version__):        
                f = open(fichero)
                for linea in f.readlines():
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
        listaFicheros = self.listar_ficheros("python")
            
        for fichero in listaFicheros:         
            if(fichero != __version__):
                for item in range(len(self.linea_de_clase)):
                    with open(fichero) as dato:
                        if(self.auxContador == len(self.linea_de_clase) - 1):
                            opcion = itertools.islice(dato,self.linea_de_clase[self.auxContador], None)

                        else:
                            opcion = itertools.islice(dato,self.linea_de_clase[self.auxContador], self.linea_de_clase[self.auxContador + 1] - 1)

                        for linea in opcion:
                            linea = linea.replace(' ', '')
                            if(len(linea.lstrip().rstrip()) > 0):
                                if(linea[0] != "#"):
                                    if(linea[0] != '"'):
                                        if(linea != ''):
                                            self.contadorLineas+=1 
                    self.loc_de_clase.append(self.contadorLineas)  
                    self.contadorLineas = 0
                    self.auxContador+=1
        
class Principal:       
    def main():
        operacion = Operaciones()
        cont_clases = 0;
        cont_metodos = 0;
        contadorAuxiliar = 0;

        locs_total = operacion.total_lineas_de_codigo()
        operacion.locs_de_clase()

        for item in operacion.contenedor_clases_metodos:
            if item.find('class') == 0:
                operacion.contenedor_clases_metodos[contadorAuxiliar] = item + str(operacion.loc_de_clase[cont_clases])
                cont_clases+=1
            contadorAuxiliar+=1

        cont_clases = 0
        contadorAuxiliar = 0
   

        for item in operacion.contenedor_clases_metodos:
            if item.find('class') == 0:           
                cont_clases+=1
                cont_metodos = 0
                print "-----------------------------------------------------"
                print item.replace(":", '').replace('class', '').replace('\n', ': ').upper().center(50)
                
            if item.find('def') == 0: 
                cont_metodos+=1
                print str(cont_metodos) + " - " + item.replace('def', '').replace(':', '') 

            contadorAuxiliar+=1

        print "-----------------------------------------------------"
        print "LOCS del programa: " + str(locs_total)
                        
    if __name__ == '__main__':
        main()