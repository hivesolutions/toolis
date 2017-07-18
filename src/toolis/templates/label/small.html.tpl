{% extends "partials/pdf/doc.html.tpl" %}
{% block content %}
    {% for label in labels %}
        <span class="label-container">
            <table class="label small" cellpadding="4">
                <tr>
                    <td class="left" width="80">
                        <div class="label-name">{{ label.name }}</div>
                        <div class="label-description">{{ label.description }}</div>
                    </td>
                    <td class="right" width="40">
                        <img class="label-image" src="data:image/png;base64,{{ label.image.data_b64 }}" />
                    </td>
                </tr>
            </table>
        </span>
    {% endfor %}
{% endblock %}
