class insecto:
    def __init__(self, nombre, edad, habitat, dieta, tamano, color, peso, textura, num_patas):
        self.nombre = nombre
        self.edad = edad
        self.habitat = habitat
        self.dieta = dieta
        self.tamano = tamano
        self.color = color
        self.peso = peso
        self.textura = textura
        self.num_patas = num_patas
    
    def excavar(self):
        print(f"{self.nombre} está excavando!")