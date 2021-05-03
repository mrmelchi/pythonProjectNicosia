# Abrimos el archivo para lectura
archivo = open('TextoEscrito.txt', 'r')

# recorremos el archivo línea a línea
for linea in archivo:
    print(linea.rstrip())

# Si necesitamos saber si el archivo está cerrado
cerrado = archivo.closed
print('El archivo está cerrado:', cerrado)

# Cerramos el archivo
archivo.close()
cerrado = archivo.closed
print('El archivo está cerrado:', cerrado)

# Podemos abrir abrir el archivo y guardarlo en una lista
# Cada linea es un elemento de la lista

archivo= open('TextoEscrito.txt', 'r')
lista = archivo.readlines()

# Imprime la lista
print(lista)

# # Imprime cada elemento de la lista
for item in lista:
    print(item)

archivo.close()

###############################
archivo = open('letras.txt','rb+')
pos = archivo.tell()
print(pos)

# Colocamos la posición desde donde queremos leer.
# 0 La referencia es desde el inicio
# 1 La referencia es desde la posición actual
# 3 La referencia es desde el final del archivo

# Nos colocamos en la quita posición desde el inicio
archivo.seek(5,0)

# Leemos 3 caracteres
cadena = archivo.read(3).decode('utf-8')
print(cadena)

# Posición actual es 8
pos = archivo.tell()
print('Posición: ', pos)

# Avanzamos 2 posiciones desde la actual y leemos otros 3
archivo.seek(2,1)
cadena = archivo.read(3).decode('utf-8')
print(cadena)

# Ahora nos movemos desde el finaldel archivo
archivo.seek(-5,2)
pos = archivo.tell()
print('Posición: ', pos)
cadena = archivo.read(3).decode('utf-8')
print(cadena)

# cerramos el archivo
archivo.close()




