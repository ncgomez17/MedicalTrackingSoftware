#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import time
from datetime import datetime

import webapp2
from google.appengine.ext import ndb
from webapp2_extras import jinja2

from Model.diagnostico import Diagnostico
from Utils.login import comprobarLogin


class EditarDiagnostico(webapp2.RequestHandler):
    def __init__(self, request, response):
        self.initialize(request, response)
        self.jinja = jinja2.get_jinja2(app=self.app)

    def get(self):
        login, nick = comprobarLogin()
        if nick:
            try:
                self.request.GET['key']
                key = self.request.GET['key']

                diagnostico = ndb.Key(urlsafe=key).get()
                sust = {
                    "login_out_url": login,
                    "nick": nick,
                    "diagnostico": diagnostico
                }
                self.response.write(self.jinja.render_template("modificarDiagnostico.html", **sust))

            except:
                print("Error al recuperar la clave del diagnostico en el formulario de editar")
                self.redirect("/ListarDiagnosticos")
        else:
            self.redirect("/")

    def post(self):
        login, nick = comprobarLogin()
        try:
            self.request.GET['key']
            key = self.request.GET['key']
        except:
            print("Error al recuperar la clave del diagnostico en el formulario de editar")
            self.redirect("/ListarDiagnosticos")

        diagnostico = ndb.Key(urlsafe=key).get()
        diagnostico.usuario = nick
        diagnostico.nss = self.request.get("nss", "Error")
        diagnostico.nombre_paciente = self.request.get("paciente", "Error")
        diagnostico.tipo_diagnostico = self.request.get("tipo_diagnostico", "Error")
        diagnostico.observaciones = self.request.get("observaciones", "Error")
        Diagnostico.update(diagnostico)
        time.sleep(1)
        return self.redirect("/ListarDiagnosticos")


app = webapp2.WSGIApplication([
    ('/ListarDiagnosticos/EditarDiagnostico', EditarDiagnostico)
], debug=True)
