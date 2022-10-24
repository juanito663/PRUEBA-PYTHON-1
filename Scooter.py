from Tecnologia import Tecnologia
from Transporte import Transporte

class Scooter(Tecnologia,Transporte):
    def __init__(self):
        Tecnologia.__init__()
        Transporte.__init__()

    