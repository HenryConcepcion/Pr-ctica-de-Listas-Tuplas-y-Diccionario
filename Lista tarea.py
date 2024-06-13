numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numeros_pares = [num for num in numeros if num % 2 == 0]
print("Números pares:", numeros_pares)

strings = ["manzana", "banana", "pera", "uva", "fresa"]
strings_con_a = [word for word in strings if "a" in word]
print("Cadenas con 'a':", strings_con_a)

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numeros_mayores_que_5 = [num for num in numeros if num > 5]
print("Números mayores que 5:", numeros_mayores_que_5)
