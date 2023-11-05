Escriba un programa Python para verificar si un número es palíndromo o no.
 
En el sistema numérico, un número palíndromo es un número que es el mismo cuando se escribe hacia adelante o hacia atrás. Los primeros números palíndromos son 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101, 111, ...

Entrada Ejemplo: 5
Salida Esperada: Es un número de palíndromo.
 
Solución:

print("==\|\Bienvenido/|/==")
numero = input(" Digite Numero: ")

lista = list(numero)
listaReverse = [lista[i - 1] for i in range(len(lista), 0, -1)]

if lista == listaReverse:
    print("Su número es palindromo")
else:
    print("Su número NO es palindromo")
