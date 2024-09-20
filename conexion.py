import pymongo

cliente=pymongo.MongoClient("mongodb://localhost:27017/")

basedatos=cliente["evidencia"]
cita=basedatos["cita"]
consl=basedatos["consultorio"]
form=basedatos["formula"]
ips=basedatos["ips"]
med=basedatos["medico"]
pac=basedatos["paciente"]



