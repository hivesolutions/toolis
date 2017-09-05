#!/usr/bin/python
# -*- coding: utf-8 -*-

import itertools

import appier

import toolis

class LabelController(appier.Controller):

    @appier.route("/labels/30x12", "GET")
    @appier.ensure(token = "admin")
    def list_30x12(self):
        labels = self._labels(rules = False)
        label_groups = self._grouper(108, labels)
        return self.template(
            "label/left/30x12.html.tpl",
            labels = labels,
            label_groups = label_groups
        )

    @appier.route("/labels/98x40", "GET")
    @appier.ensure(token = "admin")
    def list_98x40(self):
        labels = self._labels(rules = False)
        label_groups = self._grouper(12, labels)
        return self.template(
            "label/left/98x40.html.tpl",
            labels = labels,
            label_groups = label_groups
        )

    @appier.route("/labels/70x25", "GET")
    @appier.ensure(token = "admin")
    def list_70x25(self):
        labels = self._labels(rules = False)
        label_groups = self._grouper(18, labels)
        return self.template(
            "label/right/70x25.html.tpl",
            labels = labels,
            label_groups = label_groups
        )

    @appier.route("/labels/55x45", "GET")
    @appier.ensure(token = "admin")
    def list_55x45(self):
        labels = self._labels(rules = False)
        label_groups = self._grouper(15, labels)
        return self.template(
            "label/right/55x45.html.tpl",
            labels = labels,
            label_groups = label_groups
        )

    @appier.route("/labels/90x57", "GET")
    @appier.ensure(token = "admin")
    def list_90x57(self):
        labels = self._labels(rules = False)
        label_groups = self._grouper(8, labels)
        return self.template(
            "label/right/90x57.html.tpl",
            labels = labels,
            label_groups = label_groups
        )

    @appier.route("/labels/100x50", "GET")
    @appier.ensure(token = "admin")
    def list_100x50(self):
        labels = self._labels(rules = False)
        label_groups = self._grouper(5, labels)
        return self.template(
            "label/right/100x50.html.tpl",
            labels = labels,
            label_groups = label_groups
        )

    @appier.route("/labels/145x85", "GET")
    @appier.ensure(token = "admin")
    def list_145x85(self):
        labels = self._labels(rules = False)
        label_groups = self._grouper(3, labels)
        return self.template(
            "label/right/145x85.html.tpl",
            labels = labels,
            label_groups = label_groups
        )

    @appier.route("/labels/25x70", "GET")
    @appier.ensure(token = "admin")
    def list_25x70(self):
        labels = self._labels(rules = False)
        label_groups = self._grouper(21, labels)
        return self.template(
            "label/vertical/25x70.html.tpl",
            labels = labels,
            label_groups = label_groups
        )

    @appier.route("/labels/50x100", "GET")
    @appier.ensure(token = "admin")
    def list_50x100(self):
        labels = self._labels(rules = False)
        label_groups = self._grouper(6, labels)
        return self.template(
            "label/vertical/50x100.html.tpl",
            labels = labels,
            label_groups = label_groups
        )

    @appier.route("/labels/85x145", "GET")
    @appier.ensure(token = "admin")
    def list_85x145(self):
        labels = self._labels(rules = False)
        label_groups = self._grouper(2, labels)
        return self.template(
            "label/vertical/85x145.html.tpl",
            labels = labels,
            label_groups = label_groups
        )

    @appier.route("/labels/<int:id>/image", "GET", json = True)
    @appier.ensure(token = "admin")
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

    def _grouper(self, n, iterable, fillvalue = None):
        has_iterator = hasattr(itertools, "izip_longest")
        if has_iterator: zip_longest = itertools.izip_longest #@UndefinedVariable
        else: zip_longest = itertools.zip_longest #@UndefinedVariable
        args = [iter(iterable)] * n
        iterator = zip_longest(*args, fillvalue = fillvalue)
        return list(iterator)

    def _labels(self, *args, **kwargs):
        object = appier.get_object(alias = True, find = True, limit = 0)
        kwargs.update(object)
        return self.admin_part._find_view(toolis.Label, *args, **kwargs)
