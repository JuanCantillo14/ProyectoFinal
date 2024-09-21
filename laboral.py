class Laboral:
    def __init__(self,nombre_empresa,fecha_inicial,fecha_final):
        self.nombre_empresa=nombre_empresa
        self.fecha_inicial=fecha_inicial
        self.fecha_final=fecha_final
    
    def getNombe_empresa(self):
        return self.__nombre_empresa
    
    def setNombre_empresa(self,nombre_empresa):
        self.__nombre_empresa=nombre_empresa
        
    def getFecha_inicial (self):
        return self.__fecha_inicial
    
    def setFecha_inicial (self,fecha_inicial):  
        self.__fecha_inicial=fecha_inicial  
        
    def getFecha_final (self):
        return self.__fecha_final
    
    def setFecha_final (self,fecha_final):
        self.__fecha_final=fecha_final