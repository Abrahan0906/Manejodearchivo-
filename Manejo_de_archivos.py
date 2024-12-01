print("""el manejo de archivos en python es relativamente sencillo.
se usa generalmente para manipular archivos de texto o datos de manera rápida y útil.
lo primero que se debe hacer es declarar una variable cualquiera usando el siguiente método:
ejemplo: texto = open("archivo.txt")
 """)
 
 texto = open("archivo.txt") #archivo abierto y listo para leer 
 
 print("se puede leer con texto.read()") #esto lee el archivo 
 
 print(""" una vez abierto puede ser modificado y leído, 
 pero existe un método más útil y seguro utilizando las clausulas 
 with y as, usando w para escribir o a para añadir como argumentos secundarios""")
 
 with open("archivo.txt", "w") as texto:
     archivo.write("nueva línea de texto") #esto agrega texto al archivo 
 
 print("de este modo podemos acceder a los archivos")
 print("""cabe destacar, que el archivo.txt, está en la 
 misma dirección que el archivo que ejecuta el código de Python,
 si estuviera en una dirección diferente, como por ejemplo, dentro de una carpeta aledaña,
 se escribiría su dirección de éste modo:""")
 
 
 with open("carpeta_contenedora/archivo.txt", "w") as texto:
     archivo.write("nueva línea de texto")# aquí estamos usando una carpeta a un lado del archivo 
     
 print (""" si usas la sentencia Open sin usar with, es importante cerrar
 el archivo con archivo.close(), de lo contrario, no es necesario.
 el archivo debe cerrarse para evitar que este se corrompa, para descargarlo
 de la memoria y para evitar cualquier error de ejecución""")
 