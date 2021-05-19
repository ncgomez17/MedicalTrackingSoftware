# Clase modelo de Diagnosticos

from google.appengine.ext import ndb


class Diagnostico(ndb.Model):
    usuario = ndb.StringProperty(required=True)
    nss = ndb.StringProperty(required=True)
    nombre_paciente = ndb.StringProperty(required=True)
    tipo_diagnostico = ndb.StringProperty(required=True)
    observaciones = ndb.TextProperty(required=True)
    fecha = ndb.DateProperty(auto_now_add=True)

    @ndb.transactional
    def update(diagnostico):
        return diagnostico.put()