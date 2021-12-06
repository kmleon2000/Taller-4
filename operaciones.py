import math

n1 = int(input("inserte el primer número: "))
n2 = int(input("inserte el segundo número: "))
n3 = int(input("inserte el tercer número: "))

suma = n1+n2+n3
multiplicacion = n1*n2*n3
seno = math.sin(n1)
coseno = math.cos(n2)
tangente = math.tan(n3)

print("La suma de los 3 números es: ", suma)
print("La multiplicación de los 3 números es: ",multiplicacion)
print("El Seno del primer número es: ",seno)
print("El Coseno del segundo número es: ",coseno)
print("La tangete del tercer número es: ",tangente)
