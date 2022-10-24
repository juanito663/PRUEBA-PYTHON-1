from Tecnologia import Tecnologia

class Consola(Tecnologia):
    def __init__(self,voltaje:int,precio:float,eficencia:str,marca:str,nombreConsola:str,version:str):
        super().__init__(voltaje, precio, eficencia, marca)
        self.__nombreConsola = nombreConsola
        self.__version = version

    def get_nombreConsola(self):
        return self.__nombreConsola

    def get_version(self):
        return self.__version

    def set_nombreConsola(self,nombreConsola):
        self.__nombreConsola = nombreConsola

    def set_version(self,version):
        self.__version = version 


            