import webapp2
from google.appengine.ext import ndb
from webapp2_extras import jinja2
import time
from Utils.login import comprobarLogin


class BorrarDiagnostico(webapp2.RequestHandler):
    def __init__(self, request, response):
        self.initialize(request, response)
        self.jinja = jinja2.get_jinja2(app=self.app)

    def get(self):
        login, nick = comprobarLogin()
        try:
            key = self.request.GET['key']

            if nick:
                diagnostico = ndb.Key(urlsafe=key).get()
                diagnostico.key.delete()
                time.sleep(1)
                self.redirect("/ListarDiagnosticos")
            else:
                self.redirect("/")

        except Exception:
            print("Error al recuperar la clave del diagnostico para borrar")
            self.redirect("/ListarDiagnosticos")


app = webapp2.WSGIApplication([
    ('/ListarDiagnosticos/BorrarDiagnostico', BorrarDiagnostico)
], debug=True)
