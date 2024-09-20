class Antecedentes:
    def __init__(self, patologicos, quirurgicos, alergicos,ginecologicos, obstreticos, farmalogicos, familiares):
        self.__patologicos = patologicos
        self.__quirurgicos = quirurgicos
        self.__alergicos = alergicos
        self.__ginecologicos = ginecologicos
        self.__obstreticos = obstreticos
        self.__farmalogicos = farmalogicos
        self.__familiares = familiares
    
    def getPatologicos(self):
        return self.__patologicos
    
    def setPatologicos(self, patologicos):
        self.__patologicos = patologicos
    
    def getQuirurgicos(self):
        return self.__quirurgicos
    
    def setQuirurgicos(self, quirurgicos):
        self.__quirurgicos = quirurgicos
    
    def getAlegricos(self):
        return self.__alergicos
    
    def setAlegricos(self, alergicos):
        self.__alergicos = alergicos
    
    def getGinecologicos(self):
        return self.__ginecologicos
    
    def setGinecologicos(self, ginecologicos):
        self.__ginecologicos = ginecologicos
    
    def getObstreticos(self):
        return self.__obstreticos
    
    def setObstreticos(self, obstreticos):
        self.__obstreticos = obstreticos
    
    def getFramalogicos(self):
        return self.__farmalogicos
    
    def setFramalogicos(self, farmalogicos):
        self.__farmalogicos = farmalogicos
    
    def getFamiliares(self):
        return self.__familiares
    
    def setFamiliares(self, familiares):
        self.__familiares = familiares
        