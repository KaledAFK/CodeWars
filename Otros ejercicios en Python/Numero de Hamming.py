Escribe un programa Python para crear los primeros N números de Hamming, donde N es un número positivo que ingresa el usuario.
 
En informática, los números regulares a menudo se llaman números de Hamming, los números de Hamming son números cuyos únicos factores primos son 2, 3 y 5. Es decir, los números de Hamming forman una sucesión estrictamente creciente de números que cumplen las siguientes condiciones:
 
El número 1 está en la sucesión.
Si x está en la sucesión, entonces 2x, 3x y 5x también están.
Ningún otro número está en la sucesión.
 
Los primeros números de Hamming son: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 15, 16, 18, 20, 24, 25, 27, 30, 32
 
Entrada Ejemplo: 20
Salida Esperada: Primeros veinte números de Hamming: 1 2 3 4 5 6 8 9 10 12 15 16 18 20 24 25 27 30 32 36

Solución:

lista = [2, 3, 5]
listahaming = [1]
unico = []

contador = int(input("ingresa cantidad numeros: "))
mul = 1
suma = 0
cont = 0
while (mul < 5):

    v = lista.pop(0)
    lista.insert(0, v)
    v *= mul
    listahaming.append(v)
    v = lista.pop(1)
    lista.insert(1, v)
    v *= mul
    listahaming.append(v)
    v = lista.pop(2)
    lista.insert(2, v)
    v *= mul
    listahaming.append(v)
    mul += 1

while (contador > suma):
    for n in range(1, contador + 1):
        if mul % n == 0:
            cont += 1
    if cont == 2:
        suma += 1
        mul += 1
        cont = 0
    else:
        v = lista.pop(0)
        lista.insert(0, v)
        v *= mul
        listahaming.append(v)
        v = lista.pop(1)
        lista.insert(1, v)
        v *= mul
        listahaming.append(v)
        v = lista.pop(2)
        lista.insert(2, v)
        v *= mul
        listahaming.append(v)
        suma += 1
        mul += 1
        cont = 0

for x in listahaming:
    if x not in unico:
        unico.append(x)
unico.sort()
print(unico[0:n])
