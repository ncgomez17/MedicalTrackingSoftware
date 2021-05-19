import time

import webapp2
from webapp2_extras import jinja2
from Model.registroMedico import RegistroMedico
from google.appengine.ext import ndb

from Utils.login import comprobarLogin


class BuscarRegistro(webapp2.RequestHandler):
    def __init__(self, request, response):
        # Set self.request, self.response and self.app.
        self.initialize(request, response)
        self.jinja = jinja2.get_jinja2(app=self.app)

    def post(self):
        campo_registro = self.request.get("campo_registro", "ERROR")
        login, nick = comprobarLogin()
        if nick:
            registros = RegistroMedico.query(ndb.OR(RegistroMedico.nss == campo_registro,
                                                    RegistroMedico.nombre_paciente == campo_registro))
            sust = {
                "login_out_url": login,
                "nick": nick,
                "registros": registros
            }
            self.response.write(self.jinja.render_template("gestionRegistros.html", **sust))
        else:
            self.redirect("/")


app = webapp2.WSGIApplication([
    ('/ListarRegistros/BuscarRegistro', BuscarRegistro)
], debug=True)
