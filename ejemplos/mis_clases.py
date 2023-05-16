from typing import Any
# Crear dos clases en Python
# Usted defina el nombre y los atributos
# Puede usar las mismas clases usadas en Java en los ejemplos estudiados

# clase 01

class Miclase:
    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad =  edad

    def get_nombre(self):
        return self.nombre

    def get_apellido(self):
        return self.apellido

    def get_edad(self):
        return self.edad

    def set_nombre(self, n):
        self.nombre = n

    def set_apellido(self, n):
        self.apellido = n

    def set_edad(self, n):
        self.edad = n     


    def __str__(self):
        return f"\nMi nombre es: {self.nombre} {self.apellido}\nTengo {self.edad} años..\n"      
    
# clase 02

class Miclase02:
    def __init__(self, empresa, salario):
        self.empresa = empresa
        self.salario = salario

    def get_empresa(self):
        return self.empresa

    def get_salario(self):
        return self.salario
    
    def set_empresa(self, a):
        self.empresa = a

    def set_salario(self, a):
        self.salario = a  

    def __str__(self):
        return f"\nLa empresa para la que trabaja es {self.empresa}\nPosee un salario mensual de: {self.salario:.2f} dólares..\n"         
