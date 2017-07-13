#!/usr/bin/python
# -*- coding: utf-8 -*-

import appier
import appier_extras

class ToolisApp(appier.WebApp):

    def __init__(self, *args, **kwargs):
        appier.WebApp.__init__(
            self,
            name = "toolis",
            parts = (
                appier_extras.AdminPart,
            ),
            *args, **kwargs
        )

if __name__ == "__main__":
    app = ToolisApp()
    app.serve()
else:
    __path__ = []
