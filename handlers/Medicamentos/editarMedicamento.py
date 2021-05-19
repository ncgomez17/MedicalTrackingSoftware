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
from Model.medicamentos import Medicamentos
from Utils.login import comprobarLogin


class EditarMedicamento(webapp2.RequestHandler):
    def __init__(self, request, response):
        self.initialize(request, response)
        self.jinja = jinja2.get_jinja2(app=self.app)

    def get(self):
        login, nick = comprobarLogin()
        if nick:
            try:
                self.request.GET['key']
                key = self.request.GET['key']

                medicamento = ndb.Key(urlsafe=key).get()
                sust = {
                    "login_out_url": login,
                    "nick": nick,
                    "medicamento": medicamento
                }
                self.response.write(self.jinja.render_template("modificarMedicamento.html", **sust))

            except:
                print("Error al recuperar la clave del medicamento en el formulario de editar")
                self.redirect("/ListarMedicamentos")
        else:
            self.redirect("/")

    def post(self):
        login, nick = comprobarLogin()
        try:
            self.request.GET['key']
            key = self.request.GET['key']
        except:
            print("Error al recuperar la clave del medicamento en el formulario de editar")
            self.redirect("/ListarMedicamentos")

        medicamento = ndb.Key(urlsafe=key).get()
        medicamento.usuario = nick
        medicamento.nss = self.request.get("nss", "Error")
        medicamento.nombre_paciente = self.request.get("paciente", "Error")
        medicamento.medicamento = self.request.get("medicamento", "Error")
        fecha_vencimiento = self.request.get("fechavencimiento", "Error")
        fecha_final = datetime.strptime(fecha_vencimiento, '%Y-%m-%d')
        medicamento.fecha_vencimiento = fecha_final
        Medicamentos.update(medicamento)
        time.sleep(1)
        return self.redirect("/ListarMedicamentos")


app = webapp2.WSGIApplication([
    ('/ListarMedicamentos/EditarMedicamento', EditarMedicamento)
], debug=True)
