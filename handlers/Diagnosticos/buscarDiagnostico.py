import time

import webapp2
from webapp2_extras import jinja2

from Model.diagnostico import Diagnostico
from google.appengine.ext import ndb

from Utils.login import comprobarLogin


class BuscarDiagnostico(webapp2.RequestHandler):
    def __init__(self, request, response):
        # Set self.request, self.response and self.app.
        self.initialize(request, response)
        self.jinja = jinja2.get_jinja2(app=self.app)

    def post(self):
        login, nick = comprobarLogin()
        self.diagnosticos = []
        self.key_text = self.request.get("campo_diagnostico", "ERROR").lower()
        if nick:
            Diagnostico.query(Diagnostico.usuario == nick).order(-Diagnostico.fecha).map(callback=self.lookFor)
            sust = {
                "login_out_url": login,
                "nick": nick,
                "diagnosticos": self.diagnosticos
            }
            self.response.write(self.jinja.render_template("gestionDiagnosticos.html", **sust))
        else:
            self.redirect("/")

    @ndb.tasklet
    def lookFor(self, diagnostico):
        nss = diagnostico.nss.lower()
        tipo = diagnostico.tipo_diagnostico.lower()
        if (self.key_text in tipo) or (self.key_text in nss):
            self.diagnosticos += [diagnostico]


app = webapp2.WSGIApplication([
    ('/ListarDiagnosticos/BuscarDiagnostico', BuscarDiagnostico)
], debug=True)
