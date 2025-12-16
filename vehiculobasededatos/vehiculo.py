class Vehiculo:
    def __init__(self, modelo, color, motor, num_puertas, capacidad_pasajeros, tipo_combustible):
        self.modelo = modelo
        self.color = color
        self.motor = motor
        self.num_puertas = num_puertas
        self.capacidad_pasajeros = capacidad_pasajeros
        self.tipo_combustible = tipo_combustible

    def arranque(self):
        print(f"{self.modelo} ha sido encendido y está listo para partir.")

    def apagado(self):
        print(f"{self.modelo} se ha apagado correctamente.")

    def aceleracion_frenado(self):
        print(f"{self.modelo} está acelerando y puede frenar cuando sea necesario.")

    def sistema_direccion(self):
        print(f"{self.modelo} responde al volante para cambiar de dirección.")

    def climatizacion(self):
        print(f"{self.modelo} tiene sistema de climatización funcionando.")

    def tipo_seguridad(self):
        print(f"{self.modelo} cuenta con sistemas de seguridad activos.")

    def luces(self):
        print(f"{self.modelo} tiene las luces encendidas.")

    def sistema_ventanas(self):
        print(f"{self.modelo} puede abrir y cerrar las ventanas.")

    def sistema_espejo(self):
        print(f"{self.modelo} tiene espejos ajustables para mejor visibilidad.")