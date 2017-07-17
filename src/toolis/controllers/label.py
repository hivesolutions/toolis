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

    @appier.route("/labels/<int:id>/label.small", "GET")
    def small_label(self):
        label = toolis.Label.get(
            id = id,
            fields = ("image",),
            rules = False
        )
        contents = self.template(
            "label.small.html.tpl",
            label = label
        )

        #@todo better structure this code
        contents_e = contents.encode("utf-8")
        input = appier.legacy.BytesIO(contents_e)
        output = appier.legacy.BytesIO()
        try:
            def link_callback(uri, rel):
                path = os.path.join(app.path, "static", uri)
                return path

            pisa_status = xhtml2pdf.pisa.CreatePDF(
                contents,
                dest = output,
                link_callback = link_callback
            )
            data = output.getvalue()
        finally:
            output.close()

        return self.send_file(
            contents,
            content_type = "application/pdf"
        )
