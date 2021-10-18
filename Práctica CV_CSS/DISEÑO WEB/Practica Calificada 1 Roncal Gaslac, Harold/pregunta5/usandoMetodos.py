import metodos as a


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

res4 = a.exponencial(n1,n2)
print("El exponencial es: ",res4)

res5 = a.raizPrimerNumero(n1)
print("La raiz cuadrada del primer número es: ",res5)

res6= a.raizSegundoNumero(n2)
print("La raíz cuadrada del segundo número es: ", res6)

print("---------------------------------------------")

