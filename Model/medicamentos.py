# Clase modelo de Medicamentos
from google.appengine.ext import ndb


class Medicamentos(ndb.Model):
    usuario = ndb.StringProperty(required=True)
    nss = ndb.StringProperty(required=True)
    nombre_paciente = ndb.StringProperty()
    medicamento = ndb.StringProperty(required=True)
    fecha_vencimiento = ndb.DateProperty(required=True)
    fecha = ndb.DateProperty(auto_now_add=True)

    @ndb.transactional
    def update(medicamento):
        return medicamento.put()