#!/usr/bin/python
# -*- coding: utf-8 -*-

import os

import appier

import toolis

class LabelController(appier.Controller):

    @appier.route("/labels/small", "GET")
    def list_small(self):
        labels = toolis.Label.find(rules = False)
        return self.template(
            "label/small.html.tpl",
            labels = labels
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
