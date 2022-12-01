def saludar():
    print('Saludos a todos')

nombre = 'Rafael'
print(nombre)

# Esta variable es un string
apellido = "Flores"

# Enteros
edad = 15
print(type(edad))

# Decimal
peso = 1.5
print(type(peso))

print(edad + peso)

peso = 2

is_adult = True
habilitar_noticias = False

print(nombre +' '+ apellido)
print(f'{nombre} {apellido}')

#Evitar sumar distintos tipos de datos
#nombre + edad
print(nombre + str(edad))

# Listas o arreglos o arrays
alumnos = ['Angel', 'Byron', 'Deivin', 'Diego', 15, True, edad]
print(alumnos)
print(alumnos[1])

# Diccionarios
persona = {
    'nombre': 'Rafael',
    'apellido': 'Flores',
    'genero': 'Masculino',
    'edad': 54,
    'es_adulto': True,
    'altura': 1.72
}

print(persona['altura'])
print(persona['edad'])

estudiantes = [
    {'nombre': 'Ruben', 'apellido': 'Hernández'},
    {'nombre': 'Oscar', 'apellido': 'Hernández'},
    {'nombre': 'Lester', 'apellido': 'Alvarado'},
]

print(estudiantes[1]['nombre'])