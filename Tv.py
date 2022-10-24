from Tecnologia import Tecnologia

class Tv(Tecnologia):
    def __init__(self, voltaje: int, precio: float, eficencia: str, marca: str, tamaño:float):
        super().__init__(voltaje, precio, eficencia, marca)
        self.__tamaño = tamaño

    def get_tamaño(self):
        return self.__tamaño

    def set_tamaño(self,tamaño):
        self.__tamaño = tamaño
        
