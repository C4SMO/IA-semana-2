# ordenar.py · plantilla inicial
# Paso 1: comparar dos números y mostrarlos de menor a mayor
a = int(input("Primer número: "))
b = int(input("Segundo número: "))
c = int(input("Tercer número: "))

primero = 0
segundo = 0
tercero = 0

# Bloque de a
if a <= b and a <= c:
    primero = a
elif a >= b and a >= c:
    tercero = a
else:
    segundo = a

# Bloque de b
if b <= a and b <= c:
    primero = b
elif b >= a and b >= c:
    tercero = b
else:
    segundo = b

# Bloque de c
if c <= a and c <= b:
    primero = c
elif c >= a and c >= b:
    tercero = c
else:
    segundo = c

print(f"El orden esperado es: {primero}, {segundo}, {tercero}")



# Paso 2 (con tu TL): pide un tercer número c y muestra los tres de menor a mayor.
# Solo con if, else y comparaciones: sin listas, ciclos ni sorted().