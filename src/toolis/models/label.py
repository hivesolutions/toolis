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

    attributes = appier.field(
        meta = "text",
        default = True,
        observations = """The multiple attributes that describe the label"""
    )

    code = appier.field(
        meta = "text",
        default = True,
        observations = """Internal code to be used in the barcode
        generation process"""
    )

    image = appier.field(
        type = appier.File,
        private = True,
        observations = """The image that is going to be used to visually
        describe the item associated with the label"""
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
        return ("id", -1)

    @classmethod
    @appier.operation(
        name = "Create",
        parameters = (
            ("Name", "name", str),
            ("Description", "description", str),
            ("Attributes", "attributes", "longtext"),
            ("CSV File", "file", "file"),
        )
    )
    def create_s(cls, name, description, attributes, image):
        label = cls(
            name = name,
            description = description,
            attributes = attributes,
            image = image
        )
        label.save()
        return label
