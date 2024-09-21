class Academico:
    def __init__(self,titulo,institucion,fecha_culminado):
        self.titulo=titulo
        self.Institucion=institucion
        self.fecha_culminado=fecha_culminado
        
    def getTitulo (self):
        return self.__titulo
    
    def setTitulo (self,titulo):
        self.__titulo=titulo
    
    def getInstitucion (self):
        return self.__institucion
    
    def setInstitucion (self,institucion):
        self.institucion=institucion
        
    def getFecha_culminado (self):
        return self.__fecha_culminado
    