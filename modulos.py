# Forma 1
#import reservadas
#reservadas.saludar()

# Forma 2
#from reservadas import *
#saludar()

# Forma 3
# from reservadas import saludar, nombre, apellido
# print(nombre)
# saludar()

# Forma 4
# from reservadas import saludar as s
# s()

#import sys
#print(sys.path)
#sys.path.append(r'/Users/elfitaflores/Code/curso-python-noviembre/importar')
#import os
#os.environ['PYTHONPATH'] = '/Users/elfitaflores/Code/curso-python-noviembre/importar'
#import modulo

#print(modulo.x)

# try:
#     import moduloinexistente
# except ModuleNotFoundError as e:
#     print("Ups no se pudo importar el modulo", e)

# print('hola')

# import caminar

# caminar.avanzar()

# import stripe
from sqlalchemy import *

import modulo_carpeta
print(modulo_carpeta.submodulo.y)