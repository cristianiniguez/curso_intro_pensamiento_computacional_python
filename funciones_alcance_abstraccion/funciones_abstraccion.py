def enumeracion_exhaustiva(objetivo):
    respuesta = 0
    while respuesta**2 < objetivo:
        print(respuesta)
        respuesta += 1
    if respuesta**2 == objetivo:
        print(f'La raíz cuadrada de {objetivo} es {respuesta}')
    else:
        print(f'{objetivo} no tiene una raíz cuadrada exacta')


def aproximacion_soluciones(objetivo):
    epsilon = 0.01
    paso = epsilon**2
    respuesta = 0.0
    while abs(respuesta**2 - objetivo) >= epsilon and respuesta <= objetivo:
        print(abs(respuesta**2 - objetivo), respuesta)
        respuesta += paso
    if abs(respuesta**2 - objetivo) >= epsilon:
        print(f'No se encontró la raíz cuadrada de {objetivo}')
    else:
        print(f'La raíz cuadrada de {objetivo} es {respuesta}')


def busqueda_binaria(objetivo):
    epsilon = 0.01
    bajo = 0.0
    alto = max(1.0, objetivo)
    respuesta = (alto + bajo) / 2
    while abs(respuesta**2 - objetivo) >= epsilon:
        print(f'bajo={bajo}, alto={alto}, respuesta={respuesta}')
        if respuesta**2 < objetivo:
            bajo = respuesta
        else:
            alto = respuesta
        respuesta = (alto + bajo) / 2
    print(f'La raíz cuadrada de {objetivo} es {respuesta}')


objetivo = int(input('Escoge un número: '))
opcion = int(input('''
(1) enumeración exhaustiva
(2) aproximación de soluciones
(3) búsqueda binaria
Escoge una opción: '''))

if opcion == 1:
    enumeracion_exhaustiva(objetivo)
elif opcion == 2:
    aproximacion_soluciones(objetivo)
elif opcion == 3:
    busqueda_binaria(objetivo)
else:
    print('Opción desconocida')
