#!/usr/bin/python
# -*- coding: utf-8 -*-

import appier

from . import base

class Label(base.ToolisBase):

    name = appier.field(
        default = True,
        index = "hashed",
        meta = "text",
        observations = """Name of the label to be created, this should
        be as descriptive and simple as possible"""
    )

    attributes = appier.field(
        meta = "text",
        observations = """The multiple attributes that describe the label"""
    )

    code = appier.field(
        index = "hashed",
        meta = "text",
        observations = """Internal code to be used in the barcode
        generation process"""
    )

    image = appier.field(
        type = appier.File,
        private = True,
        observations = """The image that is going to be used to visually
        describe the item associated with the label"""
    )

    image_url = appier.field(
        index = "hashed",
        meta = "image_url",
        description = "Image URL"
    )

    @classmethod
    def validate(cls):
        return super(Label, cls).validate() + [
            appier.not_null("name"),
            appier.not_empty("name"),

            appier.not_duplicate("code", cls._name())
        ]

    @classmethod
    def list_names(cls):
        return ["name", "description", "code"]

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
            ("Image", "file", "file"),
        )
    )
    def create_s(cls, name, description, attributes, image):
        label = cls(
            name = name,
            description = description,
            attributes = attributes,
            image = cls.image.type(image)
        )
        label.save()
        return label

    @classmethod
    @appier.link(name = "Small")
    def list_small_url(cls, absolute = False):
        return appier.get_app().url_for(
            "label.list_small",
            absolute = absolute
        )

    @classmethod
    @appier.link(name = "Small PDF")
    def list_small_pdf_url(cls, absolute = False):
        return appier.get_app().url_for(
            "label.list_small_pdf",
            absolute = absolute
        )

    def post_create(self):
        base.ToolisBase.post_create(self)
        self.set_code_s()
        self.set_image_url_s()

    @appier.operation(name = "Set Code")
    def set_code_s(self, force = False):
        if self.code and not force: return
        prefix = appier.conf("TOOLIS_LABEL_CODE", "%09d")
        self.code = prefix % self.id
        self.save()

    @appier.operation(name = "Set Image URL")
    def set_image_url_s(self, force = False):
        if self.image_url and not force: return
        self.image_url = self.view_image_url(absolute = True)
        self.save()

    @appier.link(name = "View Image", devel = True)
    def view_image_url(self, absolute = False):
        cls = self.__class__
        return self.owner.url_for(
            "label.image",
            id = self.id,
            absolute = absolute
        )

    @appier.link(name = "Small PDF", devel = True)
    def show_small_pdf_url(self, absolute = False):
        return self.owner.url_for(
            "label.show_small_pdf",
            id = self.id,
            absolute = absolute
        )
