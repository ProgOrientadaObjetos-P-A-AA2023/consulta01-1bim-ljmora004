from mis_clases import Miclase
# Crear dos objetos de la clase 01

# objeto 01
# crear
object01 = Miclase("Luis", "Mora", 18)
# Presentar objeto; usar el método __st__
print(str(object01))
# objeto 02
object02 = Miclase("Jose", "Sanchez", 56)
print(str(object02))


# crear ingresando valores por teclado
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = int(input("Ingrese su edad: "))

persona = Miclase(nombre, apellido, edad)

# Presentar objeto; usar el método __st__
print(str(persona))

