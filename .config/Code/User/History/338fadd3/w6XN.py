print("Giraffe\nAcademy") #backslash n es para los saltos de linea
print("Giraffe\"Academy") #backslash solo es para poder imprimir caracteres especiales de forma literal
print("Giraffe\Academy")

phrase = "Giraffe Academy" #los strings se pueden guardar en variables
print(phrase + " is cool") #concatenando strings
print(phrase.lower()) #la funcion .lower pasa todo a minúscula
print(phrase.upper()) #la funcion .upper pasa todo a mayúscula
print(phrase.isupper()) #la funcion .isupper devuelve un booleano que indica si la variable es completamente mayúscula
print(phrase.upper().isupper()) #se pueden aplicar funciones a resultados de funciones
print(len(phrase)) #la funcion len toma como parametro un string y devuelve el largo del mismo
print(phrase[0]) #con los brackets podemos indicar la posición del caracter/caracteres con el/los que queremos trabajar
print(phrase.index("G")) #funcion contraria al uso de los brackets, toma como parametro el caracter y devuelve la posición del mismo en la cadena
print(phrase.index("Acad")) #tambien funciona con subcadenas
print(phrase.replace("Giraffe, "Elephant")) 
