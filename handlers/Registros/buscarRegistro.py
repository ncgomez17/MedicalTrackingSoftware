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
        login, nick = comprobarLogin()
        self.registros = []
        self.key_text = self.request.get("campo_registro", "ERROR").lower()
        if nick:
            RegistroMedico.query(RegistroMedico.usuario == nick).order(-RegistroMedico.fecha).map(
                callback=self.lookFor)
            sust = {
                "login_out_url": login,
                "nick": nick,
                "registros": self.registros
            }
            self.response.write(self.jinja.render_template("gestionRegistros.html", **sust))
        else:
            self.redirect("/")

    @ndb.tasklet
    def lookFor(self, registro):
        nss = registro.nss.lower()
        paciente= registro.nombre_paciente.lower()
        if (self.key_text in paciente) or (self.key_text in nss):
            self.registros += [registro]

app = webapp2.WSGIApplication([
    ('/ListarRegistros/BuscarRegistro', BuscarRegistro)
], debug=True)
