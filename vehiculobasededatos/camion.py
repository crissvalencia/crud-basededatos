from vehiculo import Vehiculo

class Camion(Vehiculo):
    def __init__(self, modelo, color, motor, num_puertas, capacidad_pasajeros, tipo_combustible,
                 tonelaje_max, num_ejes, tiene_remolque, tipo_carga):
        super().__init__(modelo, color, motor, num_puertas, capacidad_pasajeros, tipo_combustible)
        self.tonelaje_max = tonelaje_max
        self.num_ejes = num_ejes
        self.tiene_remolque = tiene_remolque
        self.tipo_carga = tipo_carga
    
    def levantar_plataforma(self):
        print(f"{self.modelo} está levantando la plataforma de carga.")
    
    def transportar_carga_pesada(self):
        print(f"{self.modelo} transporta hasta {self.tonelaje_max} toneladas de carga.")
    
    def conectar_remolque(self):
        if self.tiene_remolque:
            print(f"{self.modelo} tiene el remolque conectado y listo.")
        else:
            print(f"{self.modelo} no utiliza remolque en esta configuración.")