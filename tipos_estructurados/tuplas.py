my_tuple = ()  # Tupla vacía
type(my_tuple)  # <class 'tuple'>

my_tuple = (1, 'dos', True)
my_tuple[0]  # 1
my_tuple[1]  # 'dos'

my_tuple[0] = 2  # TypeError: 'tuple' object does not support item assignment

my_tuple = (1)
type(my_tuple)  # <class 'int'>

my_tuple = (1,)
type(my_tuple)  # <class 'tuple'>

my_other_tuple = (2, 3, 4)
my_tuple += my_other_tuple
print(my_tuple)  # (1, 2, 3, 4)

x, y, z = my_other_tuple
x  # 2
y  # 3
z  # 4


def coordenadas():
    return(5, 4)


x, y = coordenadas()
print(x, y)  # 5 4
