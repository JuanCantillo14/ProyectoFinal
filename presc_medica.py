from typing import Any


class PrescripcionMedica:
    def __init__(self,fecha,servicio,diagnosticoPrincipal,diagnosticoRelacionado,nomMedicamento,dosis,descripcion,cantTiempo):
        self.__fecha=fecha
        self.__servicio=servicio
        self.__diagnosticoPrincipal=diagnosticoPrincipal
        self.__diagnosticoRelacionado=diagnosticoRelacionado
        self.__nomMedicamento=nomMedicamento
        self.__dosis=dosis
        self.__descripcion=descripcion
        self.__cantTiempo=cantTiempo
        
    def getFecha(self):
        return self.__fecha
    
    def setFecha(self,fecha):
        self.__fecha=fecha
    
    def getServicio(self):
        return self.__servicio
    
    def setServicio(self,servicio):
        self.__=servicio

    def getDiagnosticoPrincipal(self):
        return self.__diagnosticoPrincipal
    
    def setDiagnosticoPrincipal(self,diagnosticoPrincipal):
        self.__diagnosticoPrincipal=diagnosticoPrincipal
        
    def getDiagnosticoRelacionado(self):
        return self.__diagnosticoRelacionado
    
    def setDiagnosticoRelacionado(self,diagnosticoRelacionado):
        self.__diagnosticoRelacionado=diagnosticoRelacionado
        
    def getNomMedicamento(self):
        return self.__nomMedicamento
    
    def setNomMedicamento(self,nomMedicamento):
        self.__nomMedicamento=nomMedicamento
    
    def getDosis(self):
        return self.__dosis
    
    def setDosis(self,dosis):
        self.__dosis=dosis
    
    def getDescripcion(self):
        return self.__descripcion
    
    def setDescripcion(self,descripcion):
        self.__descripcion=descripcion
        
    def getCantTiempo(self):
        return self.__cantTiempo
    
    def setCanTiempo(self,cantTiempo):
        self.__cantTiempo=cantTiempo


    
    