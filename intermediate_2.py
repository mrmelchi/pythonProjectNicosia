# count nos dice la cantidad de veces que
# una subcadena aparece en un texto
mensaje ='En mi casa, en mi auto, en mi escuela, enmicado'
c = mensaje.count('mi')
print(c)
print(mensaje.count(' mi '))
print(mensaje.count('enmi'))

# endswith encuentra si una cadena finaliza o no con una
# subcadena
print(mensaje.endswith('ado'))
print(mensaje.endswith('ido'))

# capitalize pone en Mayúscula la primera letra de la cadena
mensaje2= 'hola a mis amigos'
print(mensaje2.capitalize())

# center coloca la cadena centrada y rodeada de caracteres
# hasta el tamaño requerido

print(mensaje2.center(30, '*'))
print(len(mensaje2.center(30, '*')))
print(len(mensaje2))

# find nos dice si dentro de la cadena existe determinada subcadena
# nos retorna el indice donde empieza la subcadena
# - 1 si no la encuentra
# index hace lo mismo pero lanza una excepción si no la encontró

mensaje3 = 'Me gusta jugar a las canicas'
print(mensaje3.find('jugar'))
print(mensaje3.find('empezar'))
# print(mensaje3.index('empezar')) Da error

# cuidado con los espacios en las siguientes funciones
# isalnum nos indica si la cadena es alfanumérica
# es decir si tiene una letra y un caracter numérico
# los espacios no se consideran alfabéticos
mensaje5='1020'

mensaje4 = 'Todos1010'
print(mensaje3.isalnum())
print(mensaje4.isalnum())

# isalpha nos indica si todos los caracteres son alfabéticos
# los espacios no se consideran alfabéticos
mensaje5='1020'
mensaje6='hola'

print(mensaje3.isalpha())
print(mensaje4.isalpha())
print(mensaje5.isalpha())
print(mensaje6.isalpha())

# isnum nos indica si todos los caracteres son númericos
mensaje7='3.14'
print(mensaje3.isdigit())
print(mensaje4.isdigit())
print(mensaje5.isdigit())
print(mensaje6.isdigit())
print(mensaje7.isdigit())

# replace sirve para reemplazar una subcadena dentro de la cadena
print(mensaje3.replace('gusta','encanta'))


