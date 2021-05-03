# Creamos la casena que deseamos que se guarde
cadena='Hola a todos'

# Abrimos el archivo para escritura
# Pasamos el nombre del archivo, si lo deseamos con la ruta
# Indicamos que es para escritura
archivo=open('miArchivo.txt', 'w')

# Escribimos en el archivo la información
archivo.write(cadena)

# Cerramos el archivo
archivo.close()

print('Archivo escrito')
print('-'* len('Archivo escrito'))

# Abrimos el archivo para escritura
archivo=open('TextoEscrito.txt', 'w')
s = 0
# Escribimos 5 capturas del usuario
while s<5:
    texto=input('Dame un texto: ')
    archivo.write(texto + '\n')
    s += 1

# Cerramos el archivo
archivo.close()


