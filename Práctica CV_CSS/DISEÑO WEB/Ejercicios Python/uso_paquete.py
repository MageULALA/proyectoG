import ejercicio_paquete as a


print("Ingrese el primer número")
n1 = int(input())

print("Ingrese el segundo número")
n2 = int(input())

res = a.sumar(n1,n2)
print("La suma  es: " ,res)

res1 = a.restar(n1,n2)
print("El resta  es: " ,res1)

res2 = a.dividir(n1,n2)
print("La división  es: " ,res2)

res3 = a.multiplicar(n1,n2)
print("El producto  es: " ,res3)

print("---------------------------------------------")


print("Ingrese su nombre")
nombre = str(input())

print("Ingrese su primer apellido")
pApellido = str(input())

print("Ingrese su segundo apellido")
sApellido = str(input())

print("------------------------------")


d= pApellido + " "+ sApellido +" " + nombre
print("Bienvenido al Sistema " + d)


print("-----------------------------------------")

print("Que es lo que desea realizar")

print("¿ Operaciones Matemáticas ?")
rp= str(input())


