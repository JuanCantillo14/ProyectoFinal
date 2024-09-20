class Consulta:
    def __init__(self, descripcion_E, motivo_C, diagnostico, plan_Terap,
                 epicrisis, nombre_acomp, parentesco_acomp, conclusiones):
        self.__descripcion = descripcion_E
        self.__motivo = motivo_C
        self.__diagnostico = diagnostico
        self.__planterapia = plan_Terap
        self.__epicrisis = epicrisis
        self.__nombre_acomp = nombre_acomp
        self.__parentesco_acomp = parentesco_acomp
        self.__conclusiones = conclusiones
    
    def getDescripcion(self):
        return self.__descripcion
    
    def setDescripcion(self, descripcion_E):
        self.__descripcion = descripcion_E 
    
    def getMotivo(self):
        return self.__motivo
    
    def setMotivo(self, motivo_C):
        self.__motivo = motivo_C
    
    def getDiagnostico(self):
        return self.__diagnostico
    
    def setDiagnostico(self, diagnostico):
        self.__diagnostico = diagnostico
    
    def getPlanTerapia(self):
        return self.__planterapia
    
    def setPlanTerapia(self, plan_Terap):
        self.__planterapia = plan_Terap
    
    def getEpicrisis(self):
        return self.__epicrisis
    
    def setEpicrisis(self, epicrisis):
        self.__epicrisis = epicrisis
    
    def getNombre_acomp(self):
        return self.__nombre_acomp
    
    def setNombre_acomp(self, nombre_acomp):
        self.__nombre_acomp= nombre_acomp
    
    def getParentesco_A(self):
        return self.__parentesco_acomp
    
    def setParentesco_A(self, parentesco_acomp):
        self.__parentesco_acomp = parentesco_acomp
    
    def getConsultas(self):
        return self.__conclusiones
    
    def setConsultas(self, conclusiones):
        self.__conclusiones = conclusiones
        