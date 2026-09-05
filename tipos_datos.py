# Programa: Ficha secreta del superherore
# Tipos de datos básicos

# str texto

nombre = "Capitana Python"
poder_principal = "controlar bugs con la mente"

print(nombre + "puede " + poder_principal)

# int numero entero
edad= 28
misiones_completadas = 42

print("Juan de " + str(edad) + " años tiene " + str(misiones_completadas) + " misiones completadas")

# float numero decimal
nivel_enegia = 99.8

print("Mi nivel de energia es " + str(nivel_enegia))

# bool boleano
tiene_capa = True
es_villano = False

# NoneType sin valor
compania_actual = None
print(compania_actual)

print("¿El villano tiene capa? " + str(tiene_capa))
print("La " + nombre + " es una villana? " + str(es_villano))
print()
print("======= FICHA DE SUPERHEROE =======")
print("Nombre: " + nombre)
print("Poder principal: " + poder_principal)
print("Edad: "+ str(edad))
print("Misiones completadas: " + str(misiones_completadas))
print("Nivel de energia: " + str(nivel_enegia))
print("Usa capa: " + str(tiene_capa))
print("Es villano: " + str(es_villano))
print("Tiene algun equipo: " + str(compania_actual))