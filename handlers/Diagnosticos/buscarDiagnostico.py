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
        campo_diagnostico = self.request.get("campo_diagnostico", "ERROR")
        login, nick = comprobarLogin()
        if nick:
            diagnosticos = Diagnostico.query(ndb.OR(Diagnostico.nss == campo_diagnostico,
                                                    Diagnostico.tipo_diagnostico == campo_diagnostico))
            sust = {
                "login_out_url": login,
                "nick": nick,
                "diagnosticos": diagnosticos
            }
            self.response.write(self.jinja.render_template("gestionDiagnosticos.html", **sust))
        else:
            self.redirect("/")


app = webapp2.WSGIApplication([
    ('/ListarDiagnosticos/BuscarDiagnostico', BuscarDiagnostico)
], debug=True)
