from vehiculo import Vehiculo

class Furgoneta(Vehiculo):
    def __init__(self, modelo, color, motor, num_puertas, capacidad_pasajeros, tipo_combustible,
                 capacidad_carga, largo, ancho, alto):
        super().__init__(modelo, color, motor, num_puertas, capacidad_pasajeros, tipo_combustible)
        self.capacidad_carga = capacidad_carga
        self.largo = largo
        self.ancho = ancho
        self.alto = alto
    
    def cargar_mercancia(self):
        print(f"{self.modelo} está siendo cargada con mercancía hasta {self.capacidad_carga} kg.")
    
    def abrir_puertas_traseras(self):
        print(f"{self.modelo} tiene las puertas traseras abiertas para carga y descarga.")
    
    def modo_trabajo(self):
        print(f"{self.modelo} está optimizada para transporte de carga comercial.")