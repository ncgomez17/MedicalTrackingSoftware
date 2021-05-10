# Clase modelo de Medicamentos
from google.appengine.ext import ndb


class Medicamentos(ndb.Model):
    numero_seguridad = ndb.IntegerProperty(required=True)
    nombre_paciente = ndb.StringProperty()
    medicamento = ndb.StringProperty(required=True)
    fecha_vencimento = ndb.DateProperty(required=True)
    fecha = ndb.DateProperty(auto_now_add=True)
