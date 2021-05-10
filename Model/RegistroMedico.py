# Clase modelo de RegistroMedico
from google.appengine.ext import ndb


class RegistroMedico(ndb.Model):
    nss = ndb.IntegerProperty(required=True)
    nombre_paciente = ndb.StringProperty(required=True)
    domicilio = ndb.StringProperty(required=True)
    telefono = ndb.IntegerProperty(required=True)
    cod_medico = ndb.IntegerProperty(required=True)
    nombre_medico = ndb.StringProperty(required=True)
    especialidad = ndb.StringProperty(required=True)
    observaciones = ndb.TextProperty(required=True)
    fecha = ndb.DateProperty(auto_now_add=True)
