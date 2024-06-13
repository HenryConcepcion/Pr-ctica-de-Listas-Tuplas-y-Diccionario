datos = (10, 20, 30, 40, 50)

suma = sum(datos)
print("La suma de los datos es:", suma)


producto = 1
for dato in datos:
  producto *= dato
print("El producto de los datos es:", producto)


promedio = suma / len(datos)
print("El promedio de los datos es:", promedio)