#!/usr/bin/python
# -*- coding: utf-8 -*-

import appier

from . import base

class Category(base.ToolisBase):

    name = appier.field(
        default = True,
        index = "hashed",
        meta = "text",
        observations = """Name of the category this should
        be as descriptive and simple as possible"""
    )

    @classmethod
    def validate(cls):
        return super(Category, cls).validate() + [
            appier.not_null("name"),
            appier.not_empty("name"),
            appier.not_duplicate("name", cls._name())
        ]

    @classmethod
    def list_names(cls):
        return ["name", "description"]

    @classmethod
    def _plural(cls):
        return "Categories"

    @classmethod
    def order_name(cls):
        return ("id", -1)

    @appier.view(name = "Labels")
    def labels_v(self, *args, **kwargs):
        from . import label
        kwargs["sort"] = kwargs.get("sort", [("id", -1)])
        kwargs.update(category = self.name)
        return appier.lazy_dict(
            model = label.Label,
            kwargs = kwargs,
            entities = appier.lazy(lambda: label.Label.find(*args, **kwargs)),
            page = appier.lazy(lambda: label.Label.paginate(*args, **kwargs))
        )
