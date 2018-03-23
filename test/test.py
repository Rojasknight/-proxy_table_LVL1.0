import sys
from glob import *
import fileinput

ficheros=(fich for fich in iglob("*") if fich<>sys.argv[0])
file("resultado.txt","w").writelines(fileinput.input(ficheros))