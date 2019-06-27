# https://stackoverflow.com/questions/7794208/how-can-i-remove-duplicate-words-in-a-string-with-python

def palabras_unicas(l):
    palabraU = []
    [palabraU.append(x) for x in l if x not in palabraU]
    return palabraU

# Para cambiar las palabras repetidas en una columna de una cadena
# ' '.join(palabras_unicas(contenido[i+1].get_text(" ",strip=True).split()))
