class Quirurgicos:
    def __init__(self, descripcion, anestesia, fecha_P, lugar_P):
        self.__descripcion = descripcion
        self.__anestesia = anestesia
        self.__fecha_P = fecha_P
        self.__lugar_P = lugar_P
    
    def getDescripcion(self):
        return self.__descripcion
    
    def setDescripcion(self, descripcion):
        self.__descripcion = descripcion
    
    def getAnestecia(self):
        return self.__anestesia
    
    def setAnestecia(self, anestesia):
        self.__anestesia = anestesia
    
    def getFecha_P(self):
        return self.__fecha_P
    
    def setFecha_P(self, fecha_P):
        self.__fecha_P = fecha_P
    
    def getLugar_P(self):
        return self.__lugar_P
    
    def setLugar_P(self, lugar_P):
        self.__lugar_P = lugar_P
        