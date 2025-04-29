paises_y_capitales = {
    "Panamá" : "Ciudad de Panamá",
    "Colombia" : "Bogota",
    "Venezuela" : "Caracas",
    "Perú" : "Lima",
    "Ecuador" : "Quito",
    "Brasil" : "Brasilia",
    "Bolivia" : "Sucre",
    "Paraguay" : "Asuncion",
    "Uruguay" : "Montevideo",
    "Chile" : "Santiago de Chile",
    "Argentina" : "Buenos Aires",
}


while True:
    pais = input("Dime un pais (o escribe 'salir' para terminar y mostrar diccionario invertido.): ")

    if pais.lower() == "salir":
        break

    pais_normalizado = pais.strip().capitalize()
    
    for clave in paises_y_capitales:
        if clave.lower() == pais_normalizado.lower():
            print(f"La capital de {clave} es {paises_y_capitales[clave]}.")
            break
    else:
        print("Ese pais no esta en la lista o el termino es erroneo.")

print("------------------------------------------------------------------------------------------")

valores_invertidos = {pais : clave for clave, pais in paises_y_capitales.items()}
print(f"Diccionario invertido es: {valores_invertidos}")


lista = {
    "Estudiante1" : 5,
    "Estudiante2" : 2,
    "Estudiante3" : 7,
    "Estudiante4" : 6,
    "Estudiante5" : 1,
    "Estudiante6" : 4,
    "Estudiante7" : 9,
}

print("------------------------------------------------------------------------------------------")

print(lista)
for clave, valor in lista.items():
    if valor >= 6:
        print("Aprobaste")
    else:
        print("Reprobaste.")
