#Pilas en python.

print("En Python, las pilas son herramientas que funcionan \n bajo el principio de:\n <último en entrar, primero en salir>")
print("Un ejemplo de ésto es el siguiente:")
print("definiremos una lista de libros a la que llamaremos<caja>")

#definiendo caja.

caja = ["vacía"]
print("la caja estará vacía, pero le vamos a introducir cuatro libros")

print("los libros son: cien años de soledad, \nhábitos atómicos \nEl Hobbit \nEl señor de los anillos")

#introducir libros
caja.pop()
lib1 = "cien años de soledad"
lib2 = "hábitos atómicos"
lib3 = "el Hobbit"
lib4 = "el señor de los anillos"

caja.append(lib1)
caja.append(lib2)
caja.append(lib3)
caja.append(lib4)

print("vamos a imprimirlos en el orden mencionado")
l =len(caja)

for p in range(l):
    print(caja[p])

print ("ahora, intercambiamos el orden, empezando desde el último. primero vaciamos la caja")
#vaciar caja uno por uno
for p in range(l):
    caja.pop()
    
#llenar caja uno por uno
caja.append(lib4)
caja.append(lib3)
caja.append(lib2)
caja.append(lib1)
print ("Imprimimos la caja")

for p in range(l):
    print(caja[p])

print ("de Este modo, el primer libro en entrar es el último en salir y viceversa")