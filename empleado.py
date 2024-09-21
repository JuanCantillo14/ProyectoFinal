from persona import Persona 
class Empleado (Persona):
    def __init__(self, nombres, apellidos, genero, rh, correo, telefono, tipo_doc, nro_doc, fecha_nacimiento, tipo_poblacion, ocupacion,especialidad,salario,nombre_empresa,fecha_inicial,fecha_final,titulo,institucion,fecha_culminado):
        super().__init__(nombres, apellidos, genero, rh, correo, telefono, tipo_doc, nro_doc, fecha_nacimiento, tipo_poblacion,ocupacion)
        self.__especialidad=especialidad 
        self.__salario=salario 
        self.nombre_empresa=nombre_empresa
        self.fecha_inicial=fecha_inicial
        self.fecha_final=fecha_final
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
        
        
    def getEspecialidad(self):
        return self.__especialidad
    
    def setEspecialidad(self,especialidad):
        self.__especialidad=especialidad
    
    def getSalario(self):
        return self.__salario
    
    def setSalario(self,salario):
        self.__salario=salario
        
        
        
        