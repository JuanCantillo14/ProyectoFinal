class cita :
    def __init__(self, codigo_Cita, descripcion, sede_Atencion, recomendaciones):
        self.__codigo_Cita = codigo_Cita
        self.__descripcion = descripcion
        self.__sede_Atencion = sede_Atencion
        self.__recomendaciones = recomendaciones
    
    def get_codigo_Cita(self):
        return self.__codigo_Cita
    
    def set_codigo_Cita(self, codigo_Cita):
        self.__codigo_Cita = codigo_Cita
    
    def get_descripcion(self):
        return self.__descripcion
    
    def set_descripcion(self, descripcion):
        self.__descripcion = descripcion
    
    def get_sede_Atencion(self):
        return self.__sede_Atencion
    
    def set_sede_Atencion(self, sede_Atencion):
        self.__sede_Atencion = sede_Atencion
    
    def get_recomendaciones(self):
        return self.__recomendaciones
    
    def set_recomendaciones(self, recomendaciones):
        self.__recomendaciones = recomendaciones