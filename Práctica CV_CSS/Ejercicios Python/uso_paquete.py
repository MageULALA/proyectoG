import ejercicio_paquete as a


print("Ingrese el primer número")
n1 = int(input())

print("Ingrese el segundo número")
n2 = int(input())

res = a.multiplicar(n1,n2)
print("El producto de n1 y n2 es: " ,res)