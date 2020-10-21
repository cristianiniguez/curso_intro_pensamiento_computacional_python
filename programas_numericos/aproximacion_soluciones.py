# Determinar la raíz cuadrada de un número

objetivo = int(input('Escoge un número: '))
epsilon = 0.001  # Que tan cerca queremos estar de la respuesta
paso = epsilon**2  # 0.0001 - Que tanto nos iremos acercando en cada iteracion a la respuesta
respuesta = 0.0

while abs(respuesta**2 - objetivo) >= epsilon and respuesta <= objetivo:
    print(abs(respuesta**2 - objetivo), respuesta)
    respuesta += paso

if abs(respuesta**2 - objetivo) >= epsilon:
    print(f'No se encontró la raíz cuadrada de {objetivo}')
else:
    print(f'La raíz cuadrada de {objetivo} es {respuesta}')
