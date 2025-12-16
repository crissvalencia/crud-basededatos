class pato:
    def __init__(self, nombre, edad, habitat, dieta, tamano, color, peso, puede_volar, tipo_plumaje):
        self.nombre = nombre
        self.edad = edad
        self.habitat = habitat
        self.dieta = dieta
        self.tamano = tamano
        self.color = color
        self.peso = peso
        self.puede_volar = puede_volar
        self.tipo_plumaje = tipo_plumaje
    
    def nadar(self):
        print(f"{self.nombre} está nadando!")