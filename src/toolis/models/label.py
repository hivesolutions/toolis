#!/usr/bin/python
# -*- coding: utf-8 -*-

import appier

from . import base

class Label(base.ToolisBase):

    name = appier.field(
        meta = "text",
        default = True,
        observations = """Name of the label to be created, this should
        be as descriptive and simple as possible"""
    )

    code = appier.field(
        meta = "text",
        default = True,
        observations = """Internal code to be used in the barcode
        generation process"""
    )

    @classmethod
    def validate(cls):
        return super(Label, cls).validate() + [
            appier.not_null("name"),
            appier.not_empty("name"),

            appier.not_null("code"),
            appier.not_empty("code")
        ]

    @classmethod
    def list_names(cls):
        return ["name", "code"]

    @classmethod
    def order_name(cls):
        return ("s_id", -1)
