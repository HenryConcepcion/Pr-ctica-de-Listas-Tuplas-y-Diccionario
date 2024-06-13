mi_diccionario = {"nombre": "Henry", "edad": 19, "ciudad": "Santo Domingo"}


nombre = mi_diccionario["nombre"]
print(f"Nombre: {nombre}")

edad = mi_diccionario["edad"]
print(f"Edad: {edad}")

ciudad = mi_diccionario["ciudad"]
print(f"ciudad: {ciudad}")



mi_diccionario["edad"] = 21
mi_diccionario["ciudad"] = "Santiago"
mi_diccionario["nombre"] = "Julian"

print("Diccionario modificado:")
print(mi_diccionario)