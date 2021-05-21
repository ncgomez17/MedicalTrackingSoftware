import time

import webapp2
from webapp2_extras import jinja2
from Model.medicamentos import Medicamentos
from google.appengine.ext import ndb

from Utils.login import comprobarLogin


class BuscarMedicamento(webapp2.RequestHandler):
    def __init__(self, request, response):
        # Set self.request, self.response and self.app.
        self.initialize(request, response)
        self.jinja = jinja2.get_jinja2(app=self.app)

    def post(self):
        login, nick = comprobarLogin()
        self.medicamentos = []
        self.key_text = self.request.get("campo_medicamento", "ERROR").lower()
        if nick:
            Medicamentos.query(Medicamentos.usuario == nick).order(-Medicamentos.fecha_vencimiento).map(callback=self.lookFor)
            sust = {
                "login_out_url": login,
                "nick": nick,
                "medicamentos": self.medicamentos
            }
            self.response.write(self.jinja.render_template("gestionMedicamentos.html", **sust))
        else:
            self.redirect("/")

    @ndb.tasklet
    def lookFor(self, medicamento):
        nss = medicamento.nss.lower()
        medicina = medicamento.medicamento.lower()
        if (self.key_text in medicina) or (self.key_text in nss):
            self.medicamentos += [medicamento]


app = webapp2.WSGIApplication([
    ('/ListarMedicamentos/BuscarMedicamento', BuscarMedicamento)
], debug=True)
