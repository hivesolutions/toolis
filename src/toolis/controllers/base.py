#!/usr/bin/python
# -*- coding: utf-8 -*-

import appier

class BaseController(appier.Controller):

    @appier.route("/", "GET")
    def index(self):
        return self.redirect(
            self.url_for("admin.index")
        )
