# strip elimina el exceso de espacios vacios
mensaje = '   Hola a todos   '
mCorto = mensaje.strip()

print('---'+mensaje+'---')
print('---'+mCorto+'---')

print('---'+mensaje.lstrip()+'---')
print('---'+mensaje.rstrip()+'---')

# len nos da la cantidad de caracteres de una cadema
nombre = 'Nicosio'
n = len(nombre)
print(nombre, 'tiene', n, 'caracteres')

# lower cambia todas las letras a minúscula
texto = 'Hola mis amigos'
minusculas = texto.lower()
print(minusculas)
print(texto)

# upper cambia todas las letras a mayúscula
texto = 'Hola mis amigos'
mayusculas = texto.upper()
print(mayusculas)
print(texto)

# split crea una lista s partir de la cadena
# debemos colacar el delimitador que indica
# donde hacer los cortes.
palabras = texto.split(' ')
print(palabras)

valores = '5,6,32,5,7,11'
datos = valores.split(',')
print(datos)
