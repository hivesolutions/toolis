{% extends "partials/simple.html.tpl" %}
{% block title %}Labels{% endblock %}
{% block content %}
    {% for label in labels %}
        <div class="label small">
            <td class="left">
                <div class="label-name">{{ label.name }}</div>
                <div class="label-description">{{ label.description }}</div>
            </td>
            <td class="right">
                <img class="label-image" src="data:image/png;base64,{{ label.image.data_b64 }}" />
            </td>
        </div>
    {% endfor %}
{% endblock %}
