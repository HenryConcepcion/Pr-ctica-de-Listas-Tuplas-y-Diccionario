mi_diccionario = {"nombre": "Henry", "edad": 19, "ciudad": "Santo Domingo"}


print(f"El nombre es: {mi_diccionario['nombre']}")


mi_diccionario["edad"] = 19


print(f"La edad ahora es: {mi_diccionario['edad']}")


for key, value in mi_diccionario.items():
  print(f"Clave: {key}, Valor: {value}")