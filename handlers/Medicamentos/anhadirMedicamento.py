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
from datetime import datetime
from Model.medicamentos import Medicamentos
from Utils.login import comprobarLogin


class AnhadirMedicamento(webapp2.RequestHandler):
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

            self.response.write(self.jinja.render_template("formularioMedicamento.html", **sust))
        else:
            self.redirect("/")

    def post(self):
        login, nick = comprobarLogin()
        nss = self.request.get("nss", "Error")
        paciente = self.request.get("paciente", "Error")
        medicamento = self.request.get("medicamento", "Error")
        fecha_vencimiento = self.request.get("fechavencimiento", "Error")
        fecha_final = datetime.strptime(fecha_vencimiento, '%Y-%m-%d')
        medicamento = Medicamentos(usuario=nick, nss=nss, nombre_paciente=paciente, medicamento=medicamento,
                                  fecha_vencimiento=fecha_final)
        medicamento.put()
        time.sleep(1)
        return self.redirect("/ListarMedicamentos")


app = webapp2.WSGIApplication([
    ('/ListarMedicamentos/AnhadirMedicamento', AnhadirMedicamento)
], debug=True)
