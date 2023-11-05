Escriba un programa Python para verificar si un número dado es un número de Disarium o un número infeliz.
 
Un número es disarium si la suma de sus dígitos a la potencia de su posición es igual al mismo número. Por ejemplo 135 es un número de Disariumm porque 11 + 32 + 53 = 135. Algunos otros DISARIUM son 89, 175, 518 etc.
 
Entrada Ejemplo: 25
Salida Esperada: No es un número de disario.

Solución:

t = input("Digite un numero: ")
v = 0

for i in range(len(t)):
    v = v + int(t[i]) ** (i + 1)

if t == str(v) :
    print(t + " Es un número disarium ")
else:
    print(t + " No es un número disarium ")
