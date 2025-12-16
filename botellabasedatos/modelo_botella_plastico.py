from modelo_botella import Botella

class Botella_plastico(Botella):
    def __init__(self, marca, capacidad, tapa, diseno):
        super().__init__(marca, capacidad, tapa)
        self.diseno = diseno
        self.tinte = ""
        self.material = ""

    def reciclar_botella(self, material):
        self.material = material
        print(f"La botella se va a reciclar: {material}")

    def imprimir_info_plastico(self):
        print(f"El diseño es: {self.diseno}")
        print(f"El material es: {self.material}")
        print(f"El color es: {self.tinte}")
        super().imprimir_info()
        print(f"La tapa padre es: {self.tapa}")