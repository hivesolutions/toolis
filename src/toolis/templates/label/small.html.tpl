{% extends "partials/pdf/doc.html.tpl" %}
{% block content %}
    {% for label in labels %}
        <table class="label small" cellpadding="0">
            <tr>
                <td class="left" width="120">
                    <div class="label-name">{{ label.name }}</div>
                    <div class="label-description">{{ label.description }}</div>
                </td>
                <td class="right" width="60">
                    <img class="label-image" src="data:image/png;base64,{{ label.image.data_b64 }}" />
                </td>
            </tr>
        </table>
        <div class="margin">&nbsp;</div>
    {% endfor %}
{% endblock %}
