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
from webapp2_extras import jinja2
from Model.registroMedico import RegistroMedico
from Utils.login import comprobarLogin


class AnhadirRegistro(webapp2.RequestHandler):
    def __init__(self, request, response):
        self.initialize(request, response)
        self.jinja = jinja2.get_jinja2(app=self.app)

    def get(self):
        login, nick = comprobarLogin()
        if nick:
            sust = {
                "login_out_url": login,
                "nick": nick,
            }

            self.response.write(self.jinja.render_template("formularioRegistro.html", **sust))
        else:
            self.redirect("/")

    def post(self):
        login, nick = comprobarLogin()
        nss = self.request.get("nss", "Error")
        paciente = self.request.get("paciente", "Error")
        domicilio = self.request.get("domicilio", "Error")
        telefono = self.request.get("telefono", "Error")
        cod_medico = self.request.get("codMedico", "Error")
        nombre_medico = self.request.get("nombreMedico", "Error")
        especialidad = self.request.get("especialidad", "Error")
        observaciones = self.request.get("observaciones", "Error")

        registro = RegistroMedico(usuario=nick, nss=nss, nombre_paciente=paciente, domicilio=domicilio, telefono=telefono,
                                  cod_medico=cod_medico, nombre_medico=nombre_medico, especialidad=especialidad,
                                  observaciones=observaciones)
        registro.put()
        time.sleep(1)
        return self.redirect("/ListarRegistros")


app = webapp2.WSGIApplication([
    ('/ListarRegistros/AnhadirRegistro', AnhadirRegistro)
], debug=True)
