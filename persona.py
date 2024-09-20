class Persona:
    def __init__(self,nombres,apellidos,genero,rh,correo,telefono,tipo_doc,nro_doc,fecha_nacimiento,tipo_poblacion,ocupacion):
        
        self.nombres=nombres
        self.apellidos=apellidos
        self.genero=genero
        self.rh=rh
        self.correo=correo
        self.telefono=telefono
        self.tipo_doc=tipo_doc
        self.nro_doc=nro_doc
        self.fecha_nacimiento=fecha_nacimiento
        self.tipo_poblacion=tipo_poblacion
        self.ocupacion=ocupacion
    def datosPaciente(self):
        return f'{self.nombres},{self.apellidos},{self.genero},{self.rh},{self.correo},{self.telefono},{self.tipo_doc},{self.nro_doc},{self.fecha_nacimiento},{self.tipo_poblacion},{self.ocupacion}'
    
    def getNombres(self):
        return self.nombres
    def setNombres(self,nombres):
        self.nombres=nombres
    
    def getApellidos(self):
        return self.apellidos
    def setApellidos(self,apellidos):
        self.apellidos=apellidos
        
    def getGenero(self):
        return self.genero
    def setGenero(self,genero):
        self.genero=genero
        
    def getRH(self):
        return self.rh
    def setRH(self,rh):
        self.rh=rh
        
    def getCorreo(self):
        return self.correo
    def setCorreo(self,correo):
        self.correo=correo
        
    def getTelefono(self):
        return self.telefono
    def setTelefono(self,telefono):
        self.telefono=telefono
        
    def getTipo_doc(self):
        return self.tipo_doc
    def setTipo_doc(self,tipo_doc):
        self.tipo_doc=tipo_doc

    def getNro_doc(self):
        return self.nro_doc
    def setNro_doc(self,nro_doc):
        self.nro_doc=nro_doc
        
    def getFecha_nacimiento(self):
        return self.fecha_nacimiento
    def setFecha_nacimiento(self,fecha_nacimiento):
        self.fecha_nacimiento=fecha_nacimiento
        
    def getTipo_poblacion(self):
        return self.tipo_poblacion
    def setTipo_poblacion(self,tipo_poblacion):
        self.tipo_poblacion=tipo_poblacion
        
    def getOcupacion(self):
        return self.ocupacion
    def setOcupacion(self,ocupacion):
        self.ocupacion=ocupacion