class Caballo:
    def __init__(self, nombre, edad, habitat, dieta, tamano, color, peso, pelaje, domesticado):
        self.nombre = nombre
        self.edad = edad
        self.habitat = habitat
        self.dieta = dieta
        self.tamano = tamano
        self.color = color
        self.peso = peso
        self.pelaje = pelaje
        self.domesticado = domesticado
    
    def galopar(self):
        print(f"{self.nombre} está galopando!")