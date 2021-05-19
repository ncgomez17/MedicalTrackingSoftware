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
        campo_medicamento = self.request.get("campo_medicamento", "ERROR")
        login, nick = comprobarLogin()
        if nick:
            medicamentos = Medicamentos.query(ndb.OR(Medicamentos.nss == campo_medicamento,
                                                    Medicamentos.medicamento == campo_medicamento))
            sust = {
                "login_out_url": login,
                "nick": nick,
                "medicamentos": medicamentos
            }
            self.response.write(self.jinja.render_template("gestionMedicamentos.html", **sust))
        else:
            self.redirect("/")


app = webapp2.WSGIApplication([
    ('/ListarMedicamentos/BuscarMedicamento', BuscarMedicamento)
], debug=True)
