#!/usr/bin/python
# -*- coding: utf-8 -*-

import itertools

import appier

import toolis

INCREMENTER = 10

class LabelController(appier.Controller):

    def grouper(self, n, iterable, fillvalue = None):
        args = [iter(iterable)] * n
        iterator = itertools.izip_longest(*args, fillvalue = fillvalue)
        return list(iterator)

    @appier.route("/labels/98x40", "GET")
    def list_98x40(self):
        labels = toolis.Label.find(rules = False) * INCREMENTER
        label_groups = self.grouper(12, labels)
        return self.template(
            "label/98x40.html.tpl",
            labels = labels,
            label_groups = label_groups
        )

    @appier.route("/labels/50x100", "GET")
    def list_50x100(self):
        labels = toolis.Label.find(rules = False) * INCREMENTER
        label_groups = self.grouper(12, labels)
        return self.template(
            "label/50x100.html.tpl",
            labels = labels,
            label_groups = label_groups
        )

    @appier.route("/labels/85x145", "GET")
    def list_85x145(self):
        labels = toolis.Label.find(rules = False) * INCREMENTER
        label_groups = self.grouper(2, labels)
        return self.template(
            "label/85x145.html.tpl",
            labels = labels,
            label_groups = label_groups
        )

    @appier.route("/labels/<int:id>/image", "GET", json = True)
    def image(self, id):
        label = toolis.Label.get(
            id = id,
            fields = ("image",),
            rules = False
        )
        image = label.image
        if not image: raise appier.NotFoundError(
            message = "File not found for label '%d'" % id,
            code = 404
        )
        return self.send_file(
            image.data,
            content_type = image.mime,
            etag = image.etag,
            cache = True
        )
