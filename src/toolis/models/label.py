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
        description = "Image URL",
        observations = """The URL of the image that is currently associated,
        it should be a valid absolute value"""
    )

    category = appier.field(
        type = appier.reference(
            "Category",
            name = "name"
        ),
        observations = """The logical category to which this label belongs"""
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
        return ["name", "description", "code", "category"]

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
    @appier.link(name = "Left 30x12")
    def list_30x12_url(cls, view = None, context = None, absolute = False):
        return appier.get_app().url_for(
            "label.list_30x12",
            view = view,
            context = context,
            absolute = absolute
        )

    @classmethod
    @appier.link(name = "Left 98x40")
    def list_98x40_url(cls, view = None, context = None, absolute = False):
        return appier.get_app().url_for(
            "label.list_98x40",
            view = view,
            context = context,
            absolute = absolute
        )

    @classmethod
    @appier.link(name = "Right 40x25")
    def list_40x25_url(cls, view = None, context = None, absolute = False):
        return appier.get_app().url_for(
            "label.list_40x25",
            view = view,
            context = context,
            absolute = absolute
        )

    @classmethod
    @appier.link(name = "Right 70x25")
    def list_70x25_url(cls, view = None, context = None, absolute = False):
        return appier.get_app().url_for(
            "label.list_70x25",
            view = view,
            context = context,
            absolute = absolute
        )

    @classmethod
    @appier.link(name = "Right 55x45")
    def list_55x45_url(cls, view = None, context = None, absolute = False):
        return appier.get_app().url_for(
            "label.list_55x45",
            view = view,
            context = context,
            absolute = absolute
        )

    @classmethod
    @appier.link(name = "Right 90x57")
    def list_90x57_url(cls, view = None, context = None, absolute = False):
        return appier.get_app().url_for(
            "label.list_90x57",
            view = view,
            context = context,
            absolute = absolute
        )

    @classmethod
    @appier.link(name = "Right 100x50")
    def list_100x50_url(cls, view = None, context = None, absolute = False):
        return appier.get_app().url_for(
            "label.list_100x50",
            view = view,
            context = context,
            absolute = absolute
        )

    @classmethod
    @appier.link(name = "Right 145x85")
    def list_145x85_url(cls, view = None, context = None, absolute = False):
        return appier.get_app().url_for(
            "label.list_145x85",
            view = view,
            context = context,
            absolute = absolute
        )

    @classmethod
    @appier.link(name = "Vertical 25x40")
    def list_25x40_url(cls, view = None, context = None, absolute = False):
        return appier.get_app().url_for(
            "label.list_25x40",
            view = view,
            context = context,
            absolute = absolute
        )

    @classmethod
    @appier.link(name = "Vertical 25x70")
    def list_25x70_url(cls, view = None, context = None, absolute = False):
        return appier.get_app().url_for(
            "label.list_25x70",
            view = view,
            context = context,
            absolute = absolute
        )

    @classmethod
    @appier.link(name = "Vertical 50x100")
    def list_50x100_url(cls, view = None, context = None, absolute = False):
        return appier.get_app().url_for(
            "label.list_50x100",
            view = view,
            context = context,
            absolute = absolute
        )

    @classmethod
    @appier.link(name = "Vertical 85x145")
    def list_85x145_url(cls, view = None, context = None, absolute = False):
        return appier.get_app().url_for(
            "label.list_85x145",
            view = view,
            context = context,
            absolute = absolute
        )

    def post_create(self):
        base.ToolisBase.post_create(self)
        self.set_code_s()
        self.set_image_url_s()

    def post_update(self):
        base.ToolisBase.post_update(self)
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

    @appier.operation(
        name = "Set Category",
        parameters = (
            (
                "Category",
                "category",
                appier.reference("Category", name = "name")
            ),
        )
    )
    def set_category_s(self, category):
        if not category: return
        self.category = category
        self.save()

    @appier.link(name = "View Image", devel = True)
    def view_image_url(self, absolute = False):
        cls = self.__class__
        return self.owner.url_for(
            "label.image",
            id = self.id,
            absolute = absolute
        )

    @appier.link(name = "Left 30x12")
    def list_30x12_s_url(self, absolute = False):
        return self.owner.url_for(
            "label.list_30x12",
            context = "id:equals:%d" % self.id,
            absolute = absolute
        )

    @appier.link(name = "Left 98x40")
    def list_98x40_s_url(self, view = None, context = None, absolute = False):
        return appier.get_app().url_for(
            "label.list_98x40",
            context = "id:equals:%d" % self.id,
            absolute = absolute
        )

    @appier.link(name = "Right 40x25")
    def list_40x25_s_url(self, view = None, context = None, absolute = False):
        return appier.get_app().url_for(
            "label.list_40x25",
            context = "id:equals:%d" % self.id,
            absolute = absolute
        )

    @appier.link(name = "Right 70x25")
    def list_70x25_s_url(self, view = None, context = None, absolute = False):
        return appier.get_app().url_for(
            "label.list_70x25",
            context = "id:equals:%d" % self.id,
            absolute = absolute
        )

    @appier.link(name = "Right 55x45")
    def list_55x45_s_url(self, view = None, context = None, absolute = False):
        return appier.get_app().url_for(
            "label.list_55x45",
            context = "id:equals:%d" % self.id,
            absolute = absolute
        )

    @appier.link(name = "Right 90x57")
    def list_90x57_s_url(self, view = None, context = None, absolute = False):
        return appier.get_app().url_for(
            "label.list_90x57",
            context = "id:equals:%d" % self.id,
            absolute = absolute
        )

    @appier.link(name = "Right 100x50")
    def list_100x50_s_url(self, view = None, context = None, absolute = False):
        return appier.get_app().url_for(
            "label.list_100x50",
            context = "id:equals:%d" % self.id,
            absolute = absolute
        )

    @appier.link(name = "Right 145x85")
    def list_145x85_s_url(self, view = None, context = None, absolute = False):
        return appier.get_app().url_for(
            "label.list_145x85",
            context = "id:equals:%d" % self.id,
            absolute = absolute
        )

    @appier.link(name = "Vertical 25x40")
    def list_25x40_s_url(self, view = None, context = None, absolute = False):
        return appier.get_app().url_for(
            "label.list_25x40",
            context = "id:equals:%d" % self.id,
            absolute = absolute
        )

    @appier.link(name = "Vertical 25x70")
    def list_25x70_s_url(self, view = None, context = None, absolute = False):
        return appier.get_app().url_for(
            "label.list_25x70",
            context = "id:equals:%d" % self.id,
            absolute = absolute
        )

    @appier.link(name = "Vertical 50x100")
    def list_50x100_s_url(self, view = None, context = None, absolute = False):
        return appier.get_app().url_for(
            "label.list_50x100",
            context = "id:equals:%d" % self.id,
            absolute = absolute
        )

    @appier.link(name = "Vertical 85x145")
    def list_85x145_s_url(self, view = None, context = None, absolute = False):
        return appier.get_app().url_for(
            "label.list_85x145",
            context = "id:equals:%d" % self.id,
            absolute = absolute
        )
