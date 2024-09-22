from paciente import*
from simple_colors import *
import json
import pprint
from conexion import * 


enter="-"*10
sel=0
sel2=0
selg=0
selrh=0
seltel=0
seltd=0
selpob=0
selreg=0
selh=0
selh2=0
selh3=0
while sel!=4:
    try: 
        print(">>>BIEVENIDO<<<")
        print("1. Pacientes")
        print("2. Historias Clinicas")
        print("3. Talento Humano")
        print("4. Salir")
        print(f'{enter}Seleccione una opción{enter}')
        sel=int(input())
        match sel:
            
            case 1:
                while sel2!=5:
                    sel=4
                    try:
                        print(">>>BIEVENIDO<<<")
                        print("1.Registrar paciente")
                        print("2.Consultar paciente")
                        print("3.Ver pacientes")
                        print("4.Editar datos de paciente")
                        print("5.Salir") 
                        
                        print(f'{enter}Seleccione una opcion{enter}')
                        sel2=int(input())                
                        match sel2:
                            
                            case 1:
                                n=input("Ingrese nombres del paciente: ")
                                a=input("Ingrese apellidos del paciente: ")
                                while selg!=1:
                                    gen=input("""Género del paciente
    (M) para masculino
    (F) para femenino
    (I) para indefinido
Seleccione una opción: """)
                                    p=("m","M","f","F","i","I")
                                    if gen in p:
                                        selg=1
                                        if gen=="m" or gen=="M":
                                            sexo="Masculino"
                                        elif gen=="f" or gen=="F":
                                            sexo="Femenino"
                                        else: 
                                            sexo="Indefinido"
                                    else:
                                        print("Digite una opción válida")
                                while selrh!=1:
                                    try: 
                                        r=int(input("""Tipo de sangre del paciente
    1) A+
    2) A-
    3) B+
    4) B-
    5) AB+
    6) AB-
    7) O+
    8) O-
Seleccione una opción: """))
                                        if r==1 or r==2 or r==3 or r==4 or r==5 or r==6 or r==7 or r==8:
                                            selrh=1
                                            if r==1:
                                                rhs="A+"
                                            elif r==2:
                                                rhs="A-"
                                            elif r==3:
                                                rhs="B+"                         
                                            elif r==4:
                                                rhs="B-"
                                            elif r==5:
                                                rhs="AB+"
                                            elif r==6:
                                                rhs="AB-"
                                            elif r==7:
                                                rhs="O+"
                                            elif r==8:
                                                rhs="O-"
                                        else:
                                            print("Digite una opción válida")
                                    except ValueError:
                                        print("Digite una opción válida")
                                selemail=0
                                while selemail!=1:
                                    email=input("Ingrese correo del paciente(Recuerde que debe contener el caracter '@'): ")
                                    if "@" in email:
                                        selemail=1
                                        email=email    
                                    else:
                                        print("Digite un correo válido")     

                                while seltel!=1:
                                    try: 
                                        tele=int(input("Ingrese telefono del paciente: "))
                        
                                        if len(str(tele))==10:
                                            seltel=1
                                            tel=tele
                                        else:
                                            print("Digite un telefono válido")
                                    except ValueError:
                                        print("Digite un telefono válido")
                                
                                while seltd!=1:
                                    try:
                                        td=int(input("""1) Cedula de Ciudadania
    2) Cedula de Extranjería
    3) Tarjeta de Identidad
    4) Pasaporte
Seleccione una opción: """))
                                        if td==1 or td==2 or td==3 or td==4:
                                            seltd=1
                                            if td==1: 
                                                tipdoc="Cedula de Ciudadania"
                                            elif td==2: 
                                                tipdoc="Cedula de Extranjeria"     
                                            elif td==3: 
                                                tipdoc="Tarjeta de Identidad"         
                                            else:
                                                tipdoc="Pasaporte"  
                                        else:
                                            print("Digite una opción válida")    
                                    except ValueError:
                                        print("Digite una opción válida")
                                selnrodoc=0 
                                while selnrodoc!=1:
                                    try: 
                                        nrodoc=int(input("Digite el número de documento: "))  
                                        if len(str(nrodoc))>3 and len(str(nrodoc))<11:
                                            selnrodoc=1
                                            nrodoc=nrodoc
                                        else:
                                            print("Digite un número de documento válido")
                                    except ValueError:
                                        print("Digite un número de documento válido")
                                
                                nac=input("Digite la fecha de nacimiento en formato dd/mm/aaaa: ")
                            
                                while selpob!=1:
                                    try:
                                        tp=int(input("""Tipo de población
    1) Etnias
    2) Migrantes
    3) Personas con discapacidad
    4) Adulto mayor
    5) Población indigena
    6) Victima de discriminación racial y/o religiosa
    7) Pobreza extrema
    8) Victima del conflicto armado
    9) Ninguna
Seleccione una opción: """))
                                        if tp>=1 and tp<=9:
                                            selpob=1
                                            if tp==1:
                                                tipopob="Etnias"
                                            elif tp==2:
                                                tipopob="Migrantes"
                                            elif tp==3:
                                                tipopob="Personas con discapacidad"
                                            elif tp==4:
                                                tipopob="Adulto mayor"
                                            elif tp==5:
                                                tipopob="Población indigena"
                                            elif tp==6:
                                                tipopob="Victima de discriminación racial y/o religiosa"
                                            elif tp==7:
                                                tipopob="Pobreza extrema"
                                            elif tp==8:
                                                tipopob="Victima del conflicto armado"
                                            else:
                                                tipopob="Ninguna"
                                        else:
                                            print("Digite una opción válida")
                                    except ValueError:
                                        print("Digite una opción válida")
                                ocp=input("Digite la ocupacion del paciente: ")
                                epsp=input("Digite la eps del paciente: ")
                                while selreg!=1:
                                    try: 
                                        reg=int(input("""Regimen del paciente
    1) Contributivo
    2) Subsidiado 
Seleccione una opción: """))
                                        if reg==1 or reg==2:
                                            selreg=1
                                            if reg==1:
                                                regpac="Contributivo"
                                            else: 
                                                regpac="Subsidiado"
                                        else:
                                            print("Digite una opción válida")
                                    except ValueError:
                                        print("Digite una opción válida")
                                
                                datosPer=Paciente(n,a,sexo,rhs,email,tel,tipdoc,nrodoc,nac,tipopob,ocp,epsp,regpac)
                                x={"Nombre":n,"Apellidos":a,"Sexo":sexo,"RH":rhs,"Correo":email,"Telefono":tel,"Tipo Documento":tipdoc,"Nro Documento":nrodoc,"Fecha de Nacimiento":nac,"Tipo Población":tipopob,"Ocupación":ocp,"EPS":epsp,"Regimen":regpac}
            
                                # data=json.dumps(datosPer)

                        # print(data)
                        #Crear un metodo en el otro archivo donde guarde los objetos en una lista 
                                with open ("pacientes.json","w") as p:
                                    json.dump(x,p)
                            
                            
                                with open ("pacientes.json") as f:
                                    data=json.load(f)
                            
                            
                                pac.insert_one(data)
                            
                        
                            
                            case 2:
                                id=int(input("Digite el numero de documento: "))
                                
                                cursor=pac.find({"Nro Documento":id},{'Nombre':1,'Apellidos':1,'Sexo':1,'RH':1,'Correo':1,'Telefono':1,'Fecha de Nacimiento':1,'Tipo Población':1,'Ocupación':1,'EPS':1,'Regimen':1})
                                
                                # print("..........",cursor)
                                
                                for detalle in cursor:
                                    
                                    print(f'Nombre: {detalle["Nombre"]}')
                                    print(f'Apellidos: {detalle["Apellidos"]}')
                                    print(f'Genero: {detalle["Sexo"]}')
                                    print(f'RH: {detalle["RH"]}')
                                    print(f'Correo: {detalle["Correo"]}')
                                    print(f'Telefono: {detalle["Telefono"]}')
                                    print(f'Fecha de Nacimiento: {detalle["Fecha de Nacimiento"]}')
                                    print(f'Tipo de Población: {detalle["Tipo Población"]}')
                                    print(f'Ocupacion: {detalle["Ocupación"]}')
                                    print(f'EPS: {detalle["EPS"]}')
                                    print(f'Regimen: {detalle["Regimen"]}')
                            
                            case 3:  
                        
                                consultarpacientes=pac.find({},{"Nombre":1,"Nro Documento":1,"Sexo":1})
                                for doc in consultarpacientes:
                                    pprint.pp(doc)
                            case 4:
                                selpac=0
                                while selpac!=5:
                                    print(f'{enter}Editar datos de paciente{enter}')
                                    try:
                                        idAct=int(input("Digite el numero de documento del paciente: "))
                                        verificacion=pac.find_one({"Nro Documento":idAct})
                                        if verificacion:
                                            print("1. Editar correo")
                                            print("2. Editar número de telefono")
                                            print("3. Editar ocupación")
                                            print("4. Editar tipo de régimen")
                                            print("5. Salir")
                                            try:
                                                selpac=int(input("Seleccione una opción: "))
                                                match selpac:
                                                    case 1:
                                                        nvc=0
                                                        while nvc!=1:
                                                            nuevocorreo=input("Digite el nuevo correo: ")
                                                            if "@" in nuevocorreo:
                                                                nvc=1
                                                                actualizar=pac.update_one({"Nro Documento":idAct},{"$set":{"Correo":nuevocorreo}})
                                                                print("Correo actualizado correctamente")
                                                            else: 
                                                                print("Digite un correo válido")
                                                    case 2:
                                                        nvn=0
                                                        while nvn!=1:
                                                            try:
                                                                nuevonumero=int(input("Digite el número de telefono actualizado: "))
                                                                if len(str(nuevonumero))==10:
                                                                    nvn=1
                                                                    actualizar=pac.update_one({"Nro Documento":idAct},{"$set":{"Telefono":nuevonumero}})
                                                                    print("Telefono actualizado correctamente")
                                                                else: 
                                                                    print("Digite un telefono válido")
                                                            except ValueError:
                                                                print("Digite un telefono válido")

                                                    case 3:
                                                        nuevaocp=input("Digite la ocupación actualizada: ")
                                                        actualizar=pac.update_one({"Nro Documento":idAct},{"$set":{"Ocupación":nuevaocp}})
                                                        print("Ocupación actualizada correctamente")
                                                    case 4: 
                                                        selreg1=0
                                                        while selreg1!=1:
                                                            try: 
                                                                nuevoreg=int(input("""Seleccione el tipo de regimen actualizado para el paciente:
    1) Contributivo
    2) Subsidiado 
Seleccione una opción: """))
                                                                if nuevoreg==1 or nuevoreg==2:
                                                                    selreg1=1
                                                                    if nuevoreg==1:
                                                                        regm="Contributivo"
                                                                        actualizar=pac.update_one({"Nro Documento":idAct},{"$set":{"Regimen":regm}})
                                                                        print("Regimen actualizada correctamente")
                                                                    else:
                                                                        regm="Subsidiado"
                                                                        actualizar=pac.update_one({"Nro Documento":idAct},{"$set":{"Regimen":regm}})
                                                                        print("Regimen actualizada correctamente")
                                                                else: 
                                                                    print("Digite una opción valida")
                                                            except ValueError: 
                                                                print("Digite una opción válida")

                                            except ValueError:
                                                print("Digite una opción válida")
                                        else: 
                                            print("Documento no válido")
                                    except ValueError:
                                        print("Digite un documento válida") 
                    except ValueError:
                        print("Digite una opción válida") 
            case 2:
                while selh!=3:
                    selh2=0
                    print(">>>MENÚ DE HISTORIAS CLINICAS<<<")
                    print("1.Agregar datos")
                    print("2.Consultar datos")
                    print("3.Salir")
                    print(f'{enter}Seleccione una opción{enter}')
                    selh=int(input())
                    match selh:
                        case 1:
                            while selh2!=8:
                                
                                idUsu=int(input("Digite su numero de documento: "))
                                
                                
                                
                                    
                                verificacion=pac.find_one({"Nro Documento":idUsu})
                                
                                #print(f"Resultado de la búsqueda: {verificacion}") #Esto es pa ver lo que bota el cursor (no activar, era prueba)
                                    
                                    
                                if verificacion:
                                    print(">>>MENÚ DE DATOS<<<")
                                    print("1. Vacunas")
                                    print("2. Datos antropometricos")
                                    print("3. Consulta")
                                    print("4. Procemiento quirurgicos")
                                    print("5. Antecedentes personales")
                                    print("6. Prescripccion Medica")
                                    print("7. Partos")
                                    print("8. Volver al menú anterior")
                                    print(f'{enter}Seleccione una opción{enter}')
                                    selh2=int(input())
                                        
                                    match selh2:
                                        case 1:
                                            print(">>>MENU DE VACUNACION<<<")
                                            desc=input("Digite el nombre de la vacuna aplicada: ")
                                            dosis=input("Digite la dosis aplicada: ")
                                            num_vac=int(input("Digite el número de dosis a aplicar:  "))
                                            fecha_vac=input("Digite la fecha de vacunación en formato dd/mm/aaaa: ")
                                            ref=int(input("Digite el número de refuerzos: "))
                                            selviAp=0
                                            while selviAp!=1:
                                                viaAp=int(input("""Via de aplicación
    1) Intradermica
    2) Subcutanea
    3) Intramuscular
    Digite una opción: """))
                                                
                                                if viaAp==1 or viaAp==2 or viaAp==3:
                                                    selviAp=1
                                                    if viaAp==1:
                                                        aplica="Intradermica"
                                                    elif viaAp==2: 
                                                        aplica="Subcutanea"
                                                    else:
                                                        aplica="Intramuscular"
                                                else:
                                                    print("Digite una opción válida")
                                            evAd=input("Describa si ocurrio algun evento adverso al momento de aplicar la vacuna: ")
                                            interv=input("Digite el intervalo de aplicación de la vacuna: ")
                                            
                                            
                                            x={"Nro Documento":idUsu,"Categoria":"vacunas","Descripcion":desc,"Dosis":dosis,"Nro Vacunas":num_vac,"Fecha de la Vacuna":fecha_vac,"Refuerzos":ref,"Via de aplicacion":aplica,"Eventos adversos":evAd,"Intervalo":interv}

                                            with open("vacunas.json","w") as o:
                                                json.dump(x,o)
                                                
                                            with open ("vacunas.json") as f:
                                                data=json.load(f)
                                
                                
                                            pac.insert_one(data)
                                            
            
                                            print("------------Datos cargados exitosamente------------")
                                            
                                            break
                                                
                                        case 2:
                                            print(">>>REGISTRO DATOS ANTROPOMETRICOS<<<")
                                            estatura=float(input("Digite la estatura en centimetros del paciente: "))
                                            temperatura=float(input("Digite la temperatura corporal del paciente: "))
                                            peso=float(input("Digite el peso en kg del paciente: "))
                                            imc=peso/estatura**2
                                            pulso=float(input("Digite el pulso del paciente "))
                                            frecuencia_R=float(input("Digite la frecuencia respiratoria del paciente: "))
                                            presion_A=float(input("Digite la presión arterial del paciente: "))
                                            
                                            
                                            
                                            x={"Nro Documento":idUsu,"Categoria":"antropometricos","Estatura":estatura,"Temperatura":temperatura,"Peso":peso,"IMC":imc,"Pulso":pulso,"Frecuencia respiratoria":frecuencia_R,"Presión arterial":presion_A}             
                                            
                                            with open("antropometricos.json","w") as o:
                                                json.dump(x,o)
                                                
                                            with open ("antropometricos.json") as f:
                                                data=json.load(f)
                                
                                
                                            pac.insert_one(data)
                                            
            
                                            print("------------Datos cargados exitosamente------------")
                                            
                                            break
                                            
                                        case 3:
                                            print(">>>REGISTRO DATOS DE CONSULTA<<<")
                                            descripcion=input("Escriba la descripción de la consulta: ")
                                            motivo=input("Escriba el motivo de la consulta: ")
                                            diagnostico=input("Escriba el diagnóstico: ")
                                            planterapia=input("Escriba el plan de terapia de la consulta: ")
                                            epicrisis=input("Escriba la epicrisis del paciente: ")
                                            nombre_acomp=input("Escriba el nombre del acompañante: ")
                                            parentesco_acomp=input("Escriba que parentesco tiene el acompañante: ")
                                            conclusion=input("Escriba la conclusion de la consulta: ")
                                            
                                            
                                            
                                            x={"Nro Documento":idUsu,"Categoria":"consulta","Descripción":descripcion,"Motivo de consulta":motivo,"Diagnostico":diagnostico,"Plan de terapia":planterapia,"Epicrisis":epicrisis,"Nombre del acompañante":nombre_acomp,"Parentesco del acompañante":parentesco_acomp,"Conclusiones":conclusion}
                                            
                                            with open("consulta.json","w") as o:
                                                json.dump(x,o)
                                                
                                            with open ("consulta.json") as f:
                                                data=json.load(f)
                                
                                
                                            pac.insert_one(data)
                                            
            
                                            print("------------Datos cargados exitosamente------------")
                                            
                                            break
                                        
                                        
                                        case 4:
                                            print(">>>REGISTRO DE PROCESOS QUIRURGICOS<<<")
                                            descripcion=input("Escriba la descripcion del proceso: ")
                                            anesteseia=input("Escriba la informacion de la anestesia: ")
                                            fecha_p=input("Digite la fecha del proceso en formato dd/mm/aaaa: ")
                                            lugar_p=input("Escriba en que lugar se realizo: ")
                                            
                                            x={"Nro Documento":idUsu,"Categoria":"quirurgicos","Descripción del proceso":descripcion,"Anestesia":anesteseia,"Fecha del procedimiento":fecha_p,"Lugar del procedimiento":lugar_p}
                                            
                                            with open("quirurgicos.json","w") as o:
                                                json.dump(x,o)
                                                
                                            with open ("quirurgicos.json") as f:
                                                data=json.load(f)
                                
                                
                                            pac.insert_one(data)
                                            
            
                                            print("------------Datos cargados exitosamente------------")
                                            
                                            break
                                            
                                        case 5:
                                            print(">>>REGISTRO DE ANTECEDENTES PERSONALES<<<")
                                            patologicos=input("Escriba los antecedentes patologicos: ")
                                            quirurgicos=input("Escriba los antecedentes quirurgicos: ")
                                            alergicos=input("Escriba los antecedentes alergicos: ")
                                            ginecologicos=input("Escriba los antecedentes ginecologicos: ")
                                            obstreticos=input("Escriba los antecedentes obstreticos: ")
                                            farmacologicos=input("Escriba los antecedentes farmacológicos: ")
                                            familiares=input("Escriba los antecedentes familiares: ")
                                            
                                            x={"Nro Documento":idUsu,"Categoria":"antecedentes","Antecedentes patológicos":patologicos,"Antecedentes quirúrgicos":quirurgicos,"Antecedentes alérgicos":alergicos,"Antecedentes ginecológicos":ginecologicos,"Antecedentes obstreticos":obstreticos,"Antecedentes farmacológicos":farmacologicos,"Antecedentes familiares":familiares}
                                            
                                            with open("antecedentes.json","w") as o:
                                                json.dump(x,o)
                                                
                                            with open ("antecedentes.json") as f:
                                                data=json.load(f)
                                
                                
                                            pac.insert_one(data)
                                            
            
                                            print("------------Datos cargados exitosamente------------")
                                            
                                            break
                                            
                                        case 6:
                                            print(">>>REGISTRO DE PARTOS<<<")
                                            fecha_parto=input("Digite la fecha del parto en formato dd/mm/aaaa: ")
                                            hora_parto=input("Digite la hora del parto en formato 'hh:mm': ")
                                            frecCard=input("Digite la frecuencia cardiaca de la madre: ")
                                            tensArt=input("Digite la tensión arterial de la madre: ")
                                            temp=input("Digite la temperatura corporal de la madre: ")
                                            frecResp=input("Digite la frecuencia respiratoria de la madre: ")
                                            gluc=input("Digite el nivel de glucemia de la madre: ")
                                            aspGen=input("Describa la aparencia general de la madre: ")
                                            tamFeto=float(input("Digite el tamaño del feto en cm: "))
                                            numFeto=1
                                            fetoCard=input("Digite la frecuencia cardiaca del feto: ")
                                            
                                            x={"Nro Documento":idUsu,"Categoria":"partos","Fecha del parto":fecha_parto,"Hora del parto":hora_parto,"Frecuencia Cardiaca de la madre":frecCard,"Tensión arterial de la madre":tensArt,"Temperatura corporal de la madre":temp,"Frecuencia respiratoria de la madre":frecResp,"Glucemia de la madre":gluc,"Apariencia general de la madre":aspGen,"Tamaño del feto":tamFeto,"Numero de fetos":numFeto,"Fetocardia":fetoCard}
                                            
                                            with open("partos.json","w") as o:
                                                json.dump(x,o)
                                                
                                            with open ("partos.json") as f:
                                                data=json.load(f)
                                
                                
                                            pac.insert_one(data)
                                            
            
                                            print("------------Datos cargados exitosamente------------")
                                            
                                            break
                                            
                                        case 7:
                                            print(">>>REGISTRO DE PRESCRIPCION MEDICA<<<")
                                            fecha_presc=input("Digite la fecha de la prescripción médica en formato dd/mm/aaaa: ")
                                            serv=input("Digite el nombre del servicio asociado: ")
                                            diagParcial=input("Digite el diagnóstico parcial de la prescripción médica: ")
                                            nomMed=input("Digite el nombre del medicamento: ")
                                            doss=input("Digite la dosis del medicamento: ")
                                            descr=input("Describa la vía de aplicación del medicamento por parte del paciente: ")
                                            cantTiempo=input("Digite el tiempo de uso del medicamento por parte del paciente: ")
                                            
                                            x={"Nro Documento":idUsu,"Categoria":"prescripcion","Fecha de la orden médica":fecha_presc,"Servicio asociado":serv,"Diagnóstico parcial":diagParcial,"Nombre del medicamento":nomMed,"Dosis del medicamento":doss,"Vía aplicación":descr,"Tiempo de uso":cantTiempo}
                                            
                                            with open("prescripcion.json","w") as o:
                                                json.dump(x,o)
                                                
                                            with open ("prescripcion.json") as f:
                                                data=json.load(f)
                                
                                
                                            pac.insert_one(data)
                                            
            
                                            print("------------Datos cargados exitosamente------------")
                                            
                                            break
                                            
                                else:
                                    print("Este número de documento no es válido")                      
                                    selh2=7
                        case 2:
                            while selh2!=8:
                                
                                idUsu=int(input("Digite su numero de documento: "))
                                
                                
                                
                                    
                                verificacion=pac.find_one({"Nro Documento":idUsu})
                                
                                #print(f"Resultado de la búsqueda: {verificacion}") #Esto es pa ver lo que bota el cursor (no activar, era prueba)
                                    
                                    
                                if verificacion:
                                    print(">>>MENÚ DE DATOS<<<")
                                    print("1. Consultar Vacunas")
                                    print("2. Consultar Datos antropometricos")
                                    print("3. Consultas")
                                    print("4. Consultar Procemiento quirurgicos")
                                    print("5. Consultar Antecedentes personales")
                                    print("6. Consultar Prescripccion Medica")
                                    print("7. Consultar Partos")
                                    print("8. Volver al menú anterior")
                                    print(f'{enter}Seleccione una opción{enter}')
                                    selh2=int(input())
                                        
                                    match selh2:
                                        case 1:
                                            print(">>>MENU DE VACUNACION<<<")
                                                                    
                                            cursor=pac.find({"Nro Documento":idUsu,"Categoria":"Vacunas"}) 
                                            
                                            #print("..........",cursor)
                                            
                                            for detalle in cursor:
                                                
                                                print(f'Nro Documento: {detalle["Nro Documento"]}')
                                                print(f'Categoria: {detalle["Categoria"]}')
                                                print(f'Descripcion: {detalle["Descripcion"]}')
                                                print(f'Dosis: {detalle["Dosis"]}')
                                                print(f'Nro Vacunas: {detalle["Nro Vacunas"]}')
                                                print(f'Fecha de la Vacuna: {detalle["Fecha de la Vacuna"]}')
                                                print(f'Refuerzos: {detalle["Refuerzos"]}')
                                                print(f'Via de aplicacion: {detalle["Via de aplicacion"]}')
                                                print(f'Eventos adversos: {detalle["Eventos adversos"]}')
                                                print(f'Intervalo: {detalle["Intervalo"]}')
                                                
                                                
                                        case 2:
                                            print(">>>REGISTRO DATOS ANTROPOMETRICOS<<<")
                                            
                                            cursor=pac.find({"Nro Documento":idUsu,"Categoria":"antropometricos"}) 
                                            
                                            #print("..........",cursor)
                                            
                                            for detalle in cursor:
                                                
                                                print(f'Nro Documento: {detalle["Nro Documento"]}')
                                                print(f'Categoria: {detalle["Categoria"]}')
                                                print(f'Estatura: {detalle["Estatura"]}')
                                                print(f'Temperatura: {detalle["Temperatura"]}')
                                                print(f'Peso: {detalle["Peso"]}')
                                                print(f'IMC: {detalle["IMC"]}')
                                                print(f'Pulso: {detalle["Pulso"]}')
                                                print(f'Frecuencia respiratoria: {detalle["Frecuencia respiratoria"]}')
                                                print(f'Presión arterial: {detalle["Presión arterial"]}')
                                                
                                            
                                        case 3:
                                            print(">>>REGISTRO DATOS DE CONSULTA<<<")
                                            
                                            cursor=pac.find({"Nro Documento":idUsu,"Categoria":"consulta"}) 
                                            
                                            #print("..........",cursor)
                                            
                                            for detalle in cursor:
                                                
                                                print(f'Nro Documento: {detalle["Nro Documento"]}')
                                                print(f'Categoria: {detalle["Categoria"]}')
                                                print(f'Descripción: {detalle["Descripción"]}')
                                                print(f'Motivo de consulta: {detalle["Motivo de consulta"]}')
                                                print(f'Diagnostico: {detalle["Diagnostico"]}')
                                                print(f'Plan de terapia: {detalle["Plan de terapia"]}')
                                                print(f'Epicrisis: {detalle["Epicrisis"]}')
                                                print(f'Nombre del acompañante: {detalle["Nombre del acompañante"]}')
                                                print(f'Parentesco del acompañante: {detalle["Parentesco del acompañante"]}')
                                                print(f'Conclusiones: {detalle["Conclusiones"]}')
                                                
                                        
                                        case 4:
                                            print(">>>REGISTRO DE PROCESOS QUIRURGICOS<<<")
                                            
                                            cursor=pac.find({"Nro Documento":idUsu,"Categoria":"quirurgicos"}) 
                                            
                                            #print("..........",cursor)
                                            
                                            for detalle in cursor:
                                                
                                                print(f'Nro Documento: {detalle["Nro Documento"]}')
                                                print(f'Categoria: {detalle["Categoria"]}')
                                                print(f'Descripción del proceso: {detalle["Descripción del proceso"]}')
                                                print(f'Anestesia: {detalle["Anestesia"]}')
                                                print(f'Fecha del procedimiento: {detalle["Fecha del procedimiento"]}')
                                                print(f'Lugar del procedimiento: {detalle["Lugar del procedimiento"]}')
                                            
                                        case 5:
                                            print(">>>REGISTRO DE ANTECEDENTES PERSONALES<<<")
                                            
                                            cursor=pac.find({"Nro Documento":idUsu,"Categoria":"antecedentes"}) 
                                            
                                            #print("..........",cursor)
                                            
                                            for detalle in cursor:
                                                
                                                print(f'Nro Documento: {detalle["Nro Documento"]}')
                                                print(f'Categoria: {detalle["Categoria"]}')
                                                print(f'Antecedentes patológicos: {detalle["Antecedentes patológicos"]}')
                                                print(f'Antecedentes quirúrgicos: {detalle["Antecedentes quirúrgicos"]}')
                                                print(f'Antecedentes alérgicos: {detalle["Antecedentes alérgicos"]}')
                                                print(f'Antecedentes ginecológicos: {detalle["Antecedentes ginecológicos"]}')
                                                print(f'Antecedentes obstreticos: {detalle["Antecedentes obstreticos"]}')
                                                print(f'Antecedentes farmacológicos: {detalle["Antecedentes farmacológicos"]}')
                                                print(f'Antecedentes familiares: {detalle["Antecedentes familiares"]}')
                                            
                                        case 6:
                                            print(">>>REGISTRO DE PARTOS<<<")
                                            
                                            cursor=pac.find({"Nro Documento":idUsu,"Categoria":"partos"}) 
                                            
                                            #print("..........",cursor)
                                            
                                            for detalle in cursor:
                                                
                                                print(f'Nro Documento: {detalle["Nro Documento"]}')
                                                print(f'Categoria: {detalle["Categoria"]}')
                                                print(f'Fecha del parto: {detalle["Fecha del parto"]}')
                                                print(f'Hora del parto: {detalle["Hora del parto"]}')
                                                print(f'Frecuencia Cardiaca de la madre: {detalle["Frecuencia Cardiaca de la madre"]}')
                                                print(f'Tensión arterial de la madre: {detalle["Tensión arterial de la madre"]}')
                                                print(f'Temperatura corporal de la madre: {detalle["Temperatura corporal de la madre"]}')
                                                print(f'Frecuencia respiratoria de la madre: {detalle["Frecuencia respiratoria de la madre"]}')
                                                print(f'Glucemia de la madre: {detalle["Glucemia de la madre"]}')
                                                print(f'Apariencia general de la madre: {detalle["Apariencia general de la madre"]}')
                                                print(f'Tamaño del feto: {detalle["Tamaño del feto"]}')
                                                print(f'Numero de fetos: {detalle["Numero de fetos"]}')
                                                print(f'Fetocardia: {detalle["Fetocardia"]}')
                                            
                                            
                                        case 7:
                                            print(">>>REGISTRO DE PRESCRIPCION MEDICA<<<")
                                            
                                            cursor=pac.find({"Nro Documento":idUsu,"Categoria":"prescripcion"}) 
                                            
                                            #print("..........",cursor)
                                            
                                            for detalle in cursor:
                                                
                                                print(f'Nro Documento: {detalle["Nro Documento"]}')
                                                print(f'Categoria: {detalle["Categoria"]}')
                                                print(f'Fecha de la orden médica: {detalle["Fecha de la orden médica"]}')
                                                print(f'Servicio asociado: {detalle["Servicio asociado"]}')
                                                print(f'Diagnóstico parcial: {detalle["Diagnóstico parcial"]}')
                                                print(f'Nombre del medicamento: {detalle["Nombre del medicamento"]}')
                                                print(f'Dosis del medicamento: {detalle["Dosis del medicamento"]}')
                                                print(f'Vía aplicación: {detalle["Vía aplicación"]}')
                                                print(f'Tiempo de uso: {detalle["Tiempo de uso"]}')
                                            
                                else:
                                    print("Este número de documento no es válido")                      
                                    selh2=7
    except ValueError:
        print("Digite una opción válida")