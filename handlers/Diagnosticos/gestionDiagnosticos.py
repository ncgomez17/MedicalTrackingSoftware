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

import webapp2
from webapp2_extras import jinja2
from Model.diagnostico import Diagnostico
from Utils.login import comprobarLogin


class GestionDiagnosticos(webapp2.RequestHandler):
    def __init__(self, request, response):
        self.initialize(request, response)
        self.jinja = jinja2.get_jinja2(app=self.app)

    def get(self):
        login, nick = comprobarLogin()
        diagnosticos = Diagnostico.query(Diagnostico.usuario == nick).order(-Diagnostico.fecha)
        if nick:
            sust = {
                "login_out_url": login,
                "nick": nick,
                "diagnosticos": diagnosticos
            }
            self.response.write(self.jinja.render_template("gestionDiagnosticos.html", **sust))
        else:
            self.redirect("/")


app = webapp2.WSGIApplication([
    ('/ListarDiagnosticos', GestionDiagnosticos)
], debug=True)
