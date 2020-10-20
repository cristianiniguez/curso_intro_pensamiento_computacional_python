# Cadenas

a = '123'  # '123'
b = '123' * 3  # '123123123'
c = '123' + '456'  # '123456'
d = ('Hip ' * 3) + 'Hurra'  # 'Hip Hip Hip Hurra'
e = f'{"Hip " * 3}Hurra'  # 'Hip Hip Hip Hurra'

my_str = 'Platzi'

len(my_str)  # 6

my_str[0]  # 'P'
my_str[1]  # 'l'
my_str[2]  # 'a'

my_str[2:]  # 'atzi'
my_str[:3]  # 'Pla'
my_str[:-2]  # 'Plat'
my_str[::2]  # 'Paz'

a = 'Yo amo a ' + my_str  # 'Yo amo a Platzi'
b = f'Yo amo a {my_str}'  # 'Yo amo a Platzi'


# Entradas

nombre = input('¿Cuál es tu nombre?: ')  # 'Cristian'
nombre  # 'Cristian'
print(nombre)  # 'Cristian'
print('Tu nombre es', nombre)  # 'Tu nombre es Cristian'
print(f'Tu nombre es {nombre}')  # 'Tu nombre es Cristian'

numero = input('Escribe un número: ')  # 45
numero  # '45'
print(type(numero))  # <class 'str'>

numero = int(input('Escribe un número: '))  # 45
print(type(numero))  # <class 'int'>
