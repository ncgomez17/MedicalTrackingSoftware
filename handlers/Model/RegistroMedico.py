# Clase modelo de RegistroMedico
"""Campos
----->Numero seguridad Social paciente
----->Nombre y apellidos paciente
----->Domicilio
----->Telefono
----->Código identificación médico
----->Nombre y apellidos médico
----->Especialidad
----->Observaciones
"""
from google.appengine.ext import ndb


class RegistroMedico(ndb.Model):
    numero_seguridad = ndb.IntegerProperty(required=True)
    nombre_paciente = ndb.StringProperty(required=True)
    domicilio = ndb.StringProperty(required=True)
    telefono = ndb.IntegerProperty(required=True)
    cod_medico = ndb.IntegerProperty(required=True)
    nombre_medico = ndb.StringProperty(required=True)
    especialidad = ndb.StringProperty(required=True)
    observaciones = ndb.TextProperty(required=True)
    fecha = ndb.DateProperty(auto_now_add=True)
