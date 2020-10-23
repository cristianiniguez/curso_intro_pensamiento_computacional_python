my_list = [1, 2, 3]

my_list[0]  # 1
my_list[1:]  # [2, 3]

my_list.append(4)
print(my_list)  # [1, 2, 3, 4]

my_list[0] = 'a'
print(my_list)  # ['a', 2, 3, 4]

my_list.pop()  # 4
print(my_list)  # ['a', 2, 3]

for element in my_list:
    print(element)  # a; 1; 2; 3

# Side Effect

a = [1, 2, 3]
b = a

a  # [1, 2, 3]
b  # [1, 2, 3]

id(a)  # un número en memoria
id(b)  # el mismo número de antes

c = [a, b]
c  # [[1, 2, 3], [1, 2, 3]] (una lista de listas)

a.append(5)
a  # [1, 2, 3, 5]
b  # [1, 2, 3, 5] (¡aquí también!)
c  # [[1, 2, 3, 5], [1, 2, 3, 5]] (¡dos veces!)

# Clonación

a = [1, 2, 3]
id(a)  # ...

b = a
id(b)  # = id(a)

c = list(a)
id(c)  # != id(a)

d = a[::]
id(d)  # != id(a)

# List comprehensions

my_list = list(range(100))
my_list  # [0, 1, 2, ..., 99]

double = [i * 2 for i in my_list]
double  # [0, 2, 4, ..., 198]

pares = [i for i in my_list if i % 2 == 0]
pares  # [0, 2, 4, ..., 98]
