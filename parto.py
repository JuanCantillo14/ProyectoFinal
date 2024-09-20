class Parto:
    def __init__(self, fecha, hora, fredCard,tensArterial,temperatura,frecResp,glucemia,aspecto_Gen, tamaño_Feto, numero_Feto, fetocardia): 
        self.__fecha = fecha
        self.__hora = hora
        self.__frecCard = fredCard
        self.__tensArterial= tensArterial
        self.__temperatura= temperatura
        self.__frecResp= frecResp
        self.__glucemia= glucemia
        self.__aspecto_Gen = aspecto_Gen
        self.__tamaño_Feto = tamaño_Feto
        self.__numero_Feto = numero_Feto
        self.__fetocardia = fetocardia
    def getFecha(self):
        return self.__fecha
    
    def setFecha(self, fecha):
        self.__fecha = fecha
    
    def getHora(self):
        return self.__hora
    
    def setHora(self, hora):
        self.__hora = hora
    
    def getfrec_Card(self):
        return self.__frecCard
    
    def setfred_Card(self, fredCard):
        self.__frecCard = fredCard
    
    def gettens_Arterial(self):
        return self.__tensArterial
    
    def settens_Arterial(self,tens_Arterial):
        self.__tensArterial=tens_Arterial
    
    def getTemperatura(self):
        return self.__temperatura
    
    def setTemperatura(self,temperatura):
        self.__temperatura=temperatura
    
    def getfrec_Resp(self):
        return self.__frecResp    
    
    def setfrec_Resp(self,frec_Resp):
        self.__frecResp=frec_Resp

    def getGlucemia(self):
        return self.__glucemia        

    def setGlucemia(self,glucemia):
        self.__glucemia=glucemia        
    
    def getAspecto_Gen(self):
        return self.__aspecto_Gen
    
    def setAspecto_Gen(self, aspecto_Gen):
        self.__aspecto_Gen = aspecto_Gen
    
    def getTamaño_F(self):
        return self.__tamaño_Feto
    
    def setTamaño_F(self, tamaño_Feto):
        self.__tamaño_Feto = tamaño_Feto
    
    def getNumero_F(self):
        return self.__numero_Feto
    
    def setNumero_F(self, numero_Feto):
        self.__numero_Feto = numero_Feto
    
    def getFetocardia(self):
        return self.__fetocardia
    
    def setFetocardia(self, fetocardia):
        self.__fetocardia = fetocardia
        