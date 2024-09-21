import pymongo
from empleado import *

cliente=pymongo.MongoClient("mongodb://localhost:27017/")

basedatos=cliente["evidencia"]
cita=basedatos["cita"]
consl=basedatos["consultorio"]
form=basedatos["formula"]
ips=basedatos["ips"]
med=basedatos["medico"]
pac=basedatos["paciente"]
emp=basedatos["empleado"]

def registrarEmpleado(e):
    if emp.find_one ({"nro_doc":e.getNro_doc()}):
        print("Empleado ya existente")
        return
    else :
        nuevoemple={
            "Nombres":e.getNombres(),
            "Apellidos":e.getApellidos(),
            "celuar":e.getTelefono(),
            "coreo":e.getCorreo(),
            "tipo documento":e.getTipo_doc(),
            "numero doc":e.getNro_doc(),
            "rh":e.getRH(),
            "ocupacion":e.getOcupacion(),
            "Tipo poblacion":e.getTipo_poblacion(),
            "fecha nacimiento":e.getFecha_nacimiento(),
            "Genero":e.getGenero(),
            "detalles empleado":{
                "especialidad":e.getEspecialidad() ,
                "salario":e.getSalario()
            },
            "detalles laboral":{
                "Nombre empresa":e.getNombe_empresa(),
                "fecha inicial":e.getFecha_inicial(),
                "fecha final":e.getFecha_final ()
            },
            "Detalles academico":{
                "titulo":e.getTitulo(),
                "Institucion":e.getInstitucion(),
                "fecha culminado":e.getFecha_culminado ()
            },
            }
        emp.insert_one(nuevoemple)  

def mostrarEmpleado(especialidad):
    resultados=emp.find({"detalles empleado.especialidad":especialidad})
    especialidades=[x for x in resultados] 
    return especialidades