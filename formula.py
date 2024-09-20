class medica:
    def __init__(self, codigo_F, cantidad, duracion, concentracion, medicamento, indicaciones, via_Administracion):
        self.__codigo_F = codigo_F
        self.__cantidad = cantidad
        self.__duracion = duracion
        self.__concentracion = concentracion
        self.__medicamento = medicamento
        self.__indicaciones = indicaciones
        self.__via_Administracion = via_Administracion
    
    def getCodigoF(self):
        return self.__codigo_F
    
    def setCodigoF(self, codigo_F):
        self.__codigo_F = codigo_F
    
    def getCantidad(self):
        return self.__cantidad
    
    def setCantidad(self, cantidad):
        self.__cantidad = cantidad
    
    def getDuracion(self):
        return self.__duracion
    
    def setDuracion(self, duracion):
        self.__duracion = duracion
    
    def getConcentracion(self):
        return self.__concentracion
    
    def setConcentracion(self, concentracion):
        self.__concentracion = concentracion
    
    def getMedicamento(self):
        return self.__medicamento
    
    def setMedicamento(self, medicamento):
        self.__medicamento = medicamento
    
    def getIndicaciones(self):
        return self.__indicaciones
    
    def setIndicaciones(self, indicaciones):
        self.__indicaciones = indicaciones
    
    def getViaAdministracion(self):
        return self.__via_Administracion
    
    def setViaAdministracion(self, via_administracion):
        self.__via_Administracion = via_administracion
        
        
        