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
import webapp2
from google.appengine.ext import ndb
from webapp2_extras import jinja2
from Model.registroMedico import RegistroMedico
from Utils.login import comprobarLogin


class EditarRegistro(webapp2.RequestHandler):
    def __init__(self, request, response):
        self.initialize(request, response)
        self.jinja = jinja2.get_jinja2(app=self.app)

    def get(self):
        login, nick = comprobarLogin()
        if nick:
            try:
                self.request.GET['key']
                key = self.request.GET['key']

                registro = ndb.Key(urlsafe=key).get()
                sust = {
                    "login_out_url": login,
                    "nick": nick,
                    "registro": registro
                }
                self.response.write(self.jinja.render_template("modificarRegistro.html", **sust))

            except:
                print("Error al recuperar la clave del registro en el formulario de editar")
                self.redirect("/ListarRegistros")
        else:
            self.redirect("/")

    def post(self):
        login, nick = comprobarLogin()
        try:
            self.request.GET['key']
            key = self.request.GET['key']
        except:
            print("Error al recuperar la clave del registro en el formulario de editar")
            self.redirect("/ListarRegistros")
        registro = ndb.Key(urlsafe=key).get()
        registro.usuario = nick
        registro.nss = self.request.get("nss", "Error")
        registro.nombre_paciente = self.request.get("paciente", "Error")
        registro.domicilio = self.request.get("domicilio", "Error")
        registro.telefono = self.request.get("telefono", "Error")
        registro.cod_medico = self.request.get("codMedico", "Error")
        registro.nombre_medico = self.request.get("nombreMedico", "Error")
        registro.especialidad = self.request.get("especialidad", "Error")
        registro.observaciones = self.request.get("observaciones", "Error")
        RegistroMedico.update(registro)
        time.sleep(1)
        return self.redirect("/ListarRegistros")


app = webapp2.WSGIApplication([
    ('/ListarRegistros/EditarRegistro', EditarRegistro)
], debug=True)
