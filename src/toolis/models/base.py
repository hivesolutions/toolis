#!/usr/bin/python
# -*- coding: utf-8 -*-

import appier_extras

class ToolisBase(appier_extras.admin.Base):

    @classmethod
    def is_abstract(cls):
        return True
