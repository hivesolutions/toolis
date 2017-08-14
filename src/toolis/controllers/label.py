#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import itertools

import appier

import toolis

class LabelController(appier.Controller):

    def grouper(self, n, iterable, fillvalue = None):
        args = [iter(iterable)] * n
        iterator = itertools.izip_longest(*args, fillvalue = fillvalue)
        return list(iterator)

    @appier.route("/labels/98x40", "GET")
    def list_98x40(self):
        labels = toolis.Label.find(rules = False) * 10
        label_groups = self.grouper(12, labels)
        return self.template(
            "label/98x40.html.tpl",
            labels = labels,
            label_groups = label_groups
        )

    @appier.route("/labels/large", "GET")
    def list_large(self):
        labels = toolis.Label.find(rules = False) * 10
        label_groups = self.grouper(2, labels)
        return self.template(
            "label/large.html.tpl",
            labels = labels,
            label_groups = label_groups
        )

    @appier.route("/labels/small.pdf", "GET")
    def list_small_pdf(self):
        labels = toolis.Label.find(rules = False)
        return self._pdf(
            "label/pdf/small.html.tpl",
            document = dict(),
            labels = labels
        )

    @appier.route("/labels/<int:id>/small.pdf", "GET")
    def show_small_pdf(self, id):
        label = toolis.Label.get(
            id = id,
            rules = False
        )
        return self._pdf(
            "label/pdf/small.html.tpl",
            document = dict(),
            labels = (label,)
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

    def _pdf(self, path, *args, **kwargs):
        import xhtml2pdf.pisa

        contents = self.template(path, *args, **kwargs)
        output = appier.legacy.BytesIO()
        try:
            pisa_status = xhtml2pdf.pisa.CreatePDF(
                contents,
                dest = output,
                link_callback = self.link_callback,
                show_error_as_pdf = self.is_devel()
            )
            data = output.getvalue()
        finally:
            output.close()

        if pisa_status.err: raise Exception("Error in Pisa")

        return self.send_file(
            data,
            content_type = "application/pdf"
        )

    def link_callback(self, uri, rel):
        path = os.path.join(self.static_path, uri)
        return path
