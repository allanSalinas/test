
nombre1 = input("Ingresa el primer nombre: ")
nombre2 = input("Ingresa el segundo nombre: ")
nombre3 = input("Ingresa el tercer nombre: ")
nombres = [nombre1, nombre2, nombre3]
nombre_mas_largo = max(nombres, key=len)
print("El nombre con la mayor cantidad de caracteres es:",nombre_mas_largo)
