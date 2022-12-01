# While 
i = 0
while i <= 10:
    print(i)
    i += 1

print('Ciclo roto')

# For 
alumnos = ['Adan', 'Jorge', 'Andrea', 'Gaby', 'Andrea']
for alumno in alumnos:
    print(alumno)


for alumno in alumnos:
    if alumno == 'Andrea':
        print('Encontramos a Andrea')
        break

    print(alumno)

nombrePersona = 'Rafael'
nombre_persona = 'Rafael'