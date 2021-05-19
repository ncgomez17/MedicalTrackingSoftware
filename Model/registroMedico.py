# Clase modelo de RegistroMedico
from google.appengine.ext import ndb


class RegistroMedico(ndb.Model):
    usuario = ndb.StringProperty(required=True)
    nss = ndb.StringProperty(required=True)
    nombre_paciente = ndb.StringProperty(required=True)
    domicilio = ndb.StringProperty(required=True)
    telefono = ndb.StringProperty(required=True)
    cod_medico = ndb.StringProperty(required=True)
    nombre_medico = ndb.StringProperty(required=True)
    especialidad = ndb.StringProperty(required=True)
    observaciones = ndb.TextProperty()
    fecha = ndb.DateProperty(auto_now_add=True)

    @ndb.transactional
    def update(registro):
        return registro.put()
