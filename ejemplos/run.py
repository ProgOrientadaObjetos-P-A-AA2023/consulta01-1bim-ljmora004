from mis_clases import Miclase, Miclase02
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
empresa = input("Cual es el nombre de su empresa?\n")
salario = float(input("Cual es su salario mensual?\n"))

persona = Miclase02(empresa, salario)

# Presentar objeto; usar el método __st__
print(str(persona))

