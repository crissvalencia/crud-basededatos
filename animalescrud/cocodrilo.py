class Cocodrilo:
    def __init__(self, nombre, edad, habitat, dieta, tamano, color, peso, venenoso, longitud):
        self.nombre = nombre
        self.edad = edad
        self.habitat = habitat
        self.dieta = dieta
        self.tamano = tamano
        self.color = color
        self.peso = peso
        self.venenoso = venenoso
        self.longitud = longitud
    
    def sumergirse(self):
        print(f"{self.nombre} se está sumergiendo!")