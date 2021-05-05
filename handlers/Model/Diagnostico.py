# Clase modelo de Diagnosticos
"""Campos
----->Tipo de diagnostico:enfermedad o síntoma
----->Observaciones"""

from google.appengine.ext import ndb


class RegistroMedico(ndb.Model):
    tipo_diagnostico = ndb.StringProperty(required=True)
    observaciones = ndb.TextProperty(required=True)
    fecha = ndb.DateProperty(auto_now_add=True)