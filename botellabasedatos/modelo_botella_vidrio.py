from modelo_botella import Botella

class Botella_vidrio(Botella):
    def __init__(self, marca, capacidad, tapa, color_vidrio, grosor):
        super().__init__(marca, capacidad, tapa)
        self.color_vidrio = color_vidrio
        self.grosor = grosor
        self.retornable = ""

    def reutilizar_botella(self, es_retornable):
        self.retornable = es_retornable
        print(f"La botella se puede reutilizar: {es_retornable}")

    def cambiar_retornable(self, es_retornable):
        self.retornable = es_retornable
        print(f"La botella ahora es retornable: {es_retornable}")

    def imprimir_info_vidrio(self):
        print(f"El color del vidrio es: {self.color_vidrio}")
        print(f"El grosor es: {self.grosor}")
        print(f"Es retornable: {self.retornable}")
        super().imprimir_info()
        print(f"La tapa padre es: {self.tapa}")