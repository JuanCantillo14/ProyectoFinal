from persona import *
from vacunas import *
from datosATP import *
from consulta import *
from procesosQ import *
from antecedente import *
from parto import *
from presc_medica import *
from perfil_paciente import *

class Paciente(Persona):
    def __init__(self, nombres, apellidos, genero, rh, correo, telefono, tipo_doc, nro_doc, fecha_nacimiento, tipo_poblacion, ocupacion, eps, regimen):
        super().__init__(nombres, apellidos, genero, rh, correo, telefono, tipo_doc, nro_doc, fecha_nacimiento, tipo_poblacion, ocupacion)
        self.__eps=eps
        self.__regimen=regimen
        self.__vacunacion=[]
        self.__datosantrp=[]
        self.__datosconsulta=[]
        self.__datosQ=[]
        self.__AntPer=[]
        self.__datosParto=[]
        self.__datosPrescMed=[]
        self.__datosPerfPac=[]
        
    def datosPaciente(self):
        return f'{self.nombres},{self.apellidos},{self.genero},{self.rh},{self.correo},{self.telefono},{self.tipo_doc},{self.nro_doc},{self.fecha_nacimiento},{self.tipo_poblacion},{self.ocupacion},{self.__eps},{self.__regimen}'
    
    def getEPS(self):
        return self.__eps
    def setEPS(self,eps):
        self.__eps=eps
        
    def getRegimen(self):
        return self.__regimen
    def setRegimen(self,regimen):
        self.__regimen=regimen
        
    def mostrarInfo(self):
        return f'''Nombre: {self.__nombres} {self.__apellidos}
Tipo de documento: {self.__tipo_doc}
Numero de documento: {self.__nro_doc}
Fecha de nacimiento: {self.__fecha_nacimiento}
Genero: {self.__genero}
Telefono: {self.__telefono}
Correo: {self.__correo}'''

    def agregarVacuna(self, descripcion, fecha_Vacuna, dosis, numero_vacuna, refuerzos, via_aplicacion, eventos_adversos, intervalo):
        vacuna=Vacuna(descripcion,fecha_Vacuna, dosis, numero_vacuna, refuerzos, via_aplicacion, eventos_adversos, intervalo)
        self.__vacunacion.append(vacuna)
        return f'{descripcion},{fecha_Vacuna},{dosis},{numero_vacuna},{refuerzos},{via_aplicacion},{eventos_adversos},{intervalo}'
    
    def getagregarVacuna(self):
        return self.__vacunacion
    
    def agregardatosATP(self, patologicos, quirurgicos, alegricos,ginecologicos, obstreticos, framalogicos, familiares):
        datosATP=Antecedentes(patologicos, quirurgicos, alegricos,ginecologicos, obstreticos, framalogicos, familiares)
        
        self.__datosantrp.append(datosATP)
        
    def agregarConsulta(self, descripcion_E, motivo_C, diagnostico, plan_Terap,epicrisis, nombre_acomp, parentesco_acomp, conclusiones):
        cons=Consulta(descripcion_E, motivo_C, diagnostico, plan_Terap,epicrisis, nombre_acomp, parentesco_acomp, conclusiones)
        self.__datosconsulta.append(cons)

    def getConsulta(self):
        return self.__datosconsulta
    
    def agregarProcesosQ(self, descripcion, anestesia, fecha_P, lugar_P):
        procQ=Quirurgicos(descripcion, anestesia, fecha_P, lugar_P)
        self.__datosQ.append(procQ)
        
    def getProcesosQ(self):
        return self.__datosQ
    
    def agregarAntecedentes(self, patologicos, quirurgicos, alergicos,ginecologicos, obstreticos, farmalogicos, familiares):
        ant=Antecedentes(patologicos, quirurgicos, alergicos,ginecologicos, obstreticos, farmalogicos, familiares)
        self.__AntPer.append(ant)
    
    def getAntecedentes(self):
        return self.__AntPer
    
    def agregarParto(self, fecha, hora, signos_Vit, aspecto_Gen, tamaño_Feto, numero_Feto, fetocardia):
        par=Parto(self, fecha, hora, signos_Vit, aspecto_Gen, tamaño_Feto, numero_Feto, fetocardia)
        self.__datosParto.append(par)
    
    def getParto(self):
        return self.__datosParto
    
    def agregarPrescMedica(self,fecha,servicio,diagnosticoPrincipal,diagnosticoRelacionado,nomMedicamento,dosis,descripcion,cantTiempo):
        prescmed=PrescripcionMedica(fecha,servicio,diagnosticoPrincipal,diagnosticoRelacionado,nomMedicamento,dosis,descripcion,cantTiempo)
        self.__datosPrescMed.append(prescmed)
        
    def getPrescMedica(self):
        return self.__datosPrescMed
    
    def agregarPerfilPaciente(self,tratamiento,antFamiliar,vidaSexual,cicloMenstrual,sustanciaPsicoactiva,habAlimentos,consAlcohol,habSueno):
        kevin=Perfil_Paciente(tratamiento,antFamiliar,vidaSexual,cicloMenstrual,sustanciaPsicoactiva,habAlimentos,consAlcohol,habSueno)
        self.__datosPerfPac.append(kevin)
        
    def getPerfilPaciente(self):
        return self.__datosPerfPac
    
    

