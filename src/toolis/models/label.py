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
        observations = """The multiple attributes that describe the label
        should describe a set of key to value associations"""
    )

    code = appier.field(
        index = "hashed",
        meta = "text",
        observations = """Internal code to be used in the barcode
        generation process"""
    )

    image = appier.field(
        type = appier.image(
            width = 500,
            height = 500,
            format = "jpeg"
        ),
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
    @appier.link(name = "Left 98x40")
    def list_98x40_url(cls, absolute = False):
        return appier.get_app().url_for(
            "label.list_98x40",
            absolute = absolute
        )

    @classmethod
    @appier.link(name = "Vertical 25x70")
    def list_25x70_url(cls, absolute = False):
        return appier.get_app().url_for(
            "label.list_25x70",
            absolute = absolute
        )

    @classmethod
    @appier.link(name = "Vertical 50x100")
    def list_50x100_url(cls, absolute = False):
        return appier.get_app().url_for(
            "label.list_50x100",
            absolute = absolute
        )

    @classmethod
    @appier.link(name = "Vertical 85x145")
    def list_85x145_url(cls, absolute = False):
        return appier.get_app().url_for(
            "label.list_85x145",
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
