#!/usr/bin/python
# -*- coding: utf-8 -*-

import appier

import toolis

class LabelController(appier.Controller):

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

    @appier.route("/labels/<int:id>/small.pdf", "GET")
    def small_pdf(self, id):
        label = toolis.Label.get(
            id = id,
            fields = ("image",),
            rules = False
        )
        return self._pdf(
            "label/small.html.tpl",
            document = dict(),
            label = label
        )

    def _pdf(self, path, *args, **kwargs):
        import xhtml2pdf.pisa
        contents = self.template(path, *args, **kwargs)
        output = appier.legacy.BytesIO()
        try:
            pisa_status = xhtml2pdf.pisa.CreatePDF(
                contents,
                dest = output
            )
            data = output.getvalue()
        finally:
            output.close()

        if pisa_status.err: raise Exception("Error in Pisa")

        return self.send_file(
            data,
            content_type = "application/pdf"
        )
