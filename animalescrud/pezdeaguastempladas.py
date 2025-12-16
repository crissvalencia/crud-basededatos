class pezdeaguastempladas:
    def __init__(self, nombre, edad, habitat, dieta, tamano, color, peso, forma_escama, venenoso):
        self.nombre = nombre
        self.edad = edad
        self.habitat = habitat
        self.dieta = dieta
        self.tamano = tamano
        self.color = color
        self.peso = peso
        self.forma_escama = forma_escama
        self.venenoso = venenoso
    
    def nadar(self):
        print(f"{self.nombre} está nadando!")