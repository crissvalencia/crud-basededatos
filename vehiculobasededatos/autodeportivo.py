from vehiculo import Vehiculo

class AutoDeportivo(Vehiculo):
    def __init__(self, modelo, color, motor, num_puertas, capacidad_pasajeros, tipo_combustible,
                 velocidad_maxima, aceleracion_0_100, es_convertible, tipo_transmision):
        super().__init__(modelo, color, motor, num_puertas, capacidad_pasajeros, tipo_combustible)
        self.velocidad_maxima = velocidad_maxima
        self.aceleracion_0_100 = aceleracion_0_100
        self.es_convertible = es_convertible
        self.tipo_transmision = tipo_transmision
    
    def modo_sport(self):
        print(f"{self.modelo} ha activado el modo deportivo para máximo rendimiento.")
    
    def bajar_techo(self):
        if self.es_convertible:
            print(f"{self.modelo} está bajando el techo convertible.")
        else:
            print(f"{self.modelo} no tiene techo convertible.")
    
    def aceleracion_maxima(self):
        print(f"{self.modelo} acelera de 0 a 100 km/h en {self.aceleracion_0_100} segundos.")