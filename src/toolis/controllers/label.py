#!/usr/bin/python
# -*- coding: utf-8 -*-

import itertools

import appier

import toolis

class LabelController(appier.Controller):

    def grouper(self, n, iterable, fillvalue = None):
        has_iterator = hasattr(itertools, "izip_longest")
        if has_iterator: zip_longest = itertools.izip_longest #@UndefinedVariable
        else: zip_longest = itertools.zip_longest #@UndefinedVariable
        args = [iter(iterable)] * n
        iterator = zip_longest(*args, fillvalue = fillvalue)
        return list(iterator)

    @appier.route("/labels/30x12", "GET")
    def list_30x12(self):
        labels = self._labels(rules = False)
        label_groups = self.grouper(108, labels)
        return self.template(
            "label/left/30x12.html.tpl",
            labels = labels,
            label_groups = label_groups
        )

    @appier.route("/labels/98x40", "GET")
    def list_98x40(self):
        labels = self._labels(rules = False)
        label_groups = self.grouper(12, labels)
        return self.template(
            "label/left/98x40.html.tpl",
            labels = labels,
            label_groups = label_groups
        )

    @appier.route("/labels/70x25", "GET")
    def list_70x25(self):
        labels = self._labels(rules = False)
        label_groups = self.grouper(18, labels)
        return self.template(
            "label/right/70x25.html.tpl",
            labels = labels,
            label_groups = label_groups
        )

    @appier.route("/labels/55x45", "GET")
    def list_55x45(self):
        labels = self._labels(rules = False)
        label_groups = self.grouper(15, labels)
        return self.template(
            "label/right/55x45.html.tpl",
            labels = labels,
            label_groups = label_groups
        )

    @appier.route("/labels/90x57", "GET")
    def list_90x57(self):
        labels = self._labels(rules = False)
        label_groups = self.grouper(8, labels)
        return self.template(
            "label/right/90x57.html.tpl",
            labels = labels,
            label_groups = label_groups
        )

    @appier.route("/labels/100x50", "GET")
    def list_100x50(self):
        labels = self._labels(rules = False)
        label_groups = self.grouper(5, labels)
        return self.template(
            "label/right/100x50.html.tpl",
            labels = labels,
            label_groups = label_groups
        )

    @appier.route("/labels/145x85", "GET")
    def list_145x85(self):
        labels = self._labels(rules = False)
        label_groups = self.grouper(3, labels)
        return self.template(
            "label/right/145x85.html.tpl",
            labels = labels,
            label_groups = label_groups
        )

    @appier.route("/labels/25x70", "GET")
    def list_25x70(self):
        labels = self._labels(rules = False)
        label_groups = self.grouper(21, labels)
        return self.template(
            "label/vertical/25x70.html.tpl",
            labels = labels,
            label_groups = label_groups
        )

    @appier.route("/labels/50x100", "GET")
    def list_50x100(self):
        labels = self._labels(rules = False)
        label_groups = self.grouper(6, labels)
        return self.template(
            "label/vertical/50x100.html.tpl",
            labels = labels,
            label_groups = label_groups
        )

    @appier.route("/labels/85x145", "GET")
    def list_85x145(self):
        labels = self._labels(rules = False)
        label_groups = self.grouper(2, labels)
        return self.template(
            "label/vertical/85x145.html.tpl",
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

    def _labels(self, *args, **kwargs):
        context = self.field("context", [], cast = list)
        if not context: return toolis.Label.find(*args, **kwargs)
        ids = [self.get_adapter().object_id(_id) for _id in context if _id]
        return toolis.Label.find(_id = {"$in" : ids}, *args, **kwargs)
