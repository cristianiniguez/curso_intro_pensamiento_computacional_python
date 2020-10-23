my_dict = {
    'Cristian': 23,
    'Dario': 24,
    'Mary': 22,
}

my_dict['Cristian']  # 23
my_dict['Felix']  # Error
my_dict.get('Jordan', 30)  # 30
my_dict.get('Dario', 30)  # 24

my_dict['Cristian'] = 20
my_dict  # { 'Cristian': 20, 'Dario': 24, 'Mary': 22 }

my_dict['Javier'] = 21
my_dict  # { 'Cristian': 20, 'Dario': 24, 'Mary': 22, 'Javier': 21 }

del my_dict['Javier']
my_dict  # { 'Cristian': 20, 'Dario': 24, 'Mary': 22 }

for llave in my_dict.keys():
    print(llave)  # 'Cristian'; 'Dario'; 'Mary'

for valor in my_dict.values():
    print(valor)  # 20, 24, 22

for llave, valor in my_dict.items():
    print(llave, valor)  # 'Cristian' 20; 'Dario' 24; 'Mary' 22

'Dario' in my_dict  # True
'Elard' in my_dict  # False
