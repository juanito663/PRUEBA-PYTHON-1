from Tecnologia import Tecnologia
from Transporte import Transporte

class Scooter(Tecnologia,Transporte):
    def __init__(self):
        Tecnologia.__init__()
        Transporte.__init__()


    def costoDespachoBicicleta(self):
        valorKilogramoBicicleta = 400
        CostoDespachoFinalBicicleta = valorKilogramoBicicleta * self.__peso
        costofinal = CostoDespachoFinalBicicleta + self.__precio
        print(f"${costofinal}")
    