from mis_clases import Miclase02
# Crear dos objetos de la clase 02
# objeto 01
# crear
trabajador01 = Miclase02("Apple Inc", 8479.235)
# Presentar objeto; usar el método __st__
print(str(trabajador01))

# objeto 02
trabajador02 = Miclase02("Google", 7856.5156)
# Presentar objeto; usar el método __st__
print(str(trabajador02))

# crear ingresando valores por teclado
empresa = input("Ingrese el nombre de su empresa:\n")
salario = float(input("Ingrese su salario mensual:\n"))

trabajador03 = Miclase02(empresa, salario)

# Presentar objeto; usar el método __st__
print(str(trabajador03))


