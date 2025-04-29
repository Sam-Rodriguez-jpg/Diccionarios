Auto = {
    "Marca" : "Toyota",
    "Modelo" : "Supra",
    "Año" : 1998,
}

print(Auto)

Auto["Modelo"] = "Corolla"
Auto["Color"] = "Rojo"
del Auto["Año"]

print(Auto)

for Clave, Valor in Auto.items():
    print(f"La clave es: {Clave}")

for Clave, Valor in Auto.items():
    print(f"Los valor del diccionario es: {Valor}")