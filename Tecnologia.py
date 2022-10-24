class Tecnologia:
    def __init__(self,voltaje:int,precio:float,eficencia:str,marca:str):
        self.__voltaje = voltaje
        self.__precio = precio
        self.__eficencia = eficencia
        self.__marca = marca
        
    def get_voltaje(self):
        return self.__voltaje     
    
    def get_precio(self):
        return self.__precio
    
    def get_eficencia(self):
        return self.__eficencia

    def get_marca(self):
        return self.__marca

    def set_voltaje(self,voltaje):
        self.__voltaje = voltaje

    def set_precio(self,precio):
        self.__precio = precio

    def set_eficencia(self,eficencia):
        self.__eficencia = eficencia

    def set_marca(self,marca):
        self.__marca = marca
    
    def calcularDescuento(self):
        if self.__eficencia == "a" or self.__eficencia == "b" or self.__eficencia == "A" or self.__eficencia == "B":
            descuento = self.__precio * 0.5
            precioFinal = self.__precio - descuento
            print(f'el descuento es de 50% y su precio total es de:{precioFinal} , el precio sin el descuento es de: {self.__precio}')
        
        elif self.__eficencia == "c" or self.__eficencia == "d" or self.__eficencia == "C" or self.__eficencia == "D":
            descuento = self.__precio * 0.3
            precioFinal =  self.__precio - descuento
            print(f'el descuento es de 30% y su precio total es de:{precioFinal} , el precio sin el descuento es de: {self.__precio}')
            
        
        elif self.__eficencia == "e" or self.__eficencia == "f" or self.__eficencia == "E" or self.__eficencia == "F":
            descuento = self.__precio * 0.1
            precioFinal = self.__precio - descuento
            self.set_precio(precioFinal)
            print (f'el descuento es de 10% y su precio total es de:{precioFinal} , el precio sin el descuento es de: {self.__precio}')

        else:
            print("no se genero ningun descuento")

    
