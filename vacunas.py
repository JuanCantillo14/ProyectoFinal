class Vacuna:
    def __init__(self, descripcion, fecha_Vacuna, dosis, numero_vacuna, refuerzos, via_aplicacion, eventos_adversos, intervalo):
         self.__descripcion = descripcion
         self.__fecha_Vacuna = fecha_Vacuna
         self.__dosis = dosis
         self.__numero_vacuna = numero_vacuna
         self.__refuerzos = refuerzos
         self.__via_aplicacion = via_aplicacion
         self.__eventos_adversos = eventos_adversos
         self.__intervalo = intervalo
             
    def getDescipción(self):
        return self.__descripcion
    
    def setDescipción(self,descripcion):
        self.__descripcion = descripcion
    
    def getFecha_Vacuna(self):
        return self.__fecha_Vacuna
    
    def setFecha_Vacuna(self, fecha_Vacuna):
        self.__fecha_Vacuna = fecha_Vacuna
        
    def getDosis(self):
        return self.__dosis
    
    def setDosis(self, dosis):
        self.__dosis = dosis
        
    def getNumero_Vacuna(self):
        return self.__numero_vacuna
    
    def setNumero_Vacuna(self, numero_vacuna):
        self.__numero_vacuna = numero_vacuna
        
    def getRefuerzos(self):
        return self.__refuerzos
    
    def setRefuerzos(self, refuerzos):
        self.__refuerzos = refuerzos
    
    def getVia_Aplicacion(self):
        return self.__via_aplicacion
    
    def setVia_Aplicacion(self, via_aplicacion):
        self.__via_aplicacion = via_aplicacion
        
    def getEventos_adversos(self):
        return self.__eventos_adversos
    
    def setEventos_Adversos(self, eventos_adversos):
        self.__eventos_adversos = eventos_adversos
        
    def getIntervalo(self):
        return self.__intervalo
    
    def setIntervalo(self, intervalo):
        self.__intervalo = intervalo
        
        