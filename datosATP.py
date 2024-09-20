class antropometricos:
    def __init__(self, talla,temperatura,imc,pulso, peso, frecuencia_R, presion_A):
        self.__peso = peso
        self.__temperatura = temperatura
        self.__talla = talla
        self.__imc= imc
        self.__pulso = pulso
        self.__frecuencia_R = frecuencia_R
        self.__presion_A = presion_A
    
    def getPeso(self):
        return self.__peso
    
    def setPeso(self, peso):
        self.__peso = peso
    
    def getTemperatura(self):
        return self.__temperatura
    
    def setTemperatura(self, temperatura):
        self.__temperatura = temperatura
    
    def getTalla(self):
        return self.__talla
    
    def setTalla(self, talla):
        self.__talla = talla
    
    def getIMC(self):
        return self.__imc
    
    def setIMC(self, imc):
        self.__imc = imc
        
    def getPluso(self):
        return self.__pulso
    
    def setPluso(self, pulso):
        self.__pulso = pulso
    
    def getFrecuencia_R(self):
        return self.__frecuencia_R
    
    def setFrecuencia_R(self, frecuencia_R):
        self.__frecuencia_R = frecuencia_R
    
    def getPresion_A(self):
        return self.__presion_A
    
    def setPresion_A(self, presion_A):
        self.__presion_A = presion_A
        