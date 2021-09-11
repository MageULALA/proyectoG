
#Listas
lista1 = ["Espejo","Silla","Mesa","Televisor"]
lista2 = ["Pijama","Terno","Pantalón","Camisa"]
lista3 = ["Caballo","Pollo","Abeja","Ganza"]
lista4 = ["Juan","Pedro","Luis","Mario"]


#Tuplas
tupla1 = 1,2,3,4 
tupla2 = ("Pizarra","Plumón","Mota","Regla") 
tupla3= tupla2,"Perú","Chile","Colombia" 

#Sets
conjunto = set() 
muebles = set(lista1) 
ropa = set(lista2)
print ("Mesa Plegable" in muebles) 
print ("gorros" in ropa)


#Diccionario

animales = {'Perro':'Carnivoro',
              'Vaca':'Herbívoro',
              'Iguana':'Anfibio'}
print('El perro es un animal', animales['Perro'])  

armas = {'AK47':'arma de largo alcance',
              'Pistola ':'arma de corto alcance',
              'cuchillo':'arma de mano'}
print('El arma más poderosa es', armas['AK47'])  