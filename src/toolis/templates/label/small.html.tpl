{% extends "partials/simple.html.tpl" %}
{% block title %}Labels{% endblock %}
{% block content %}
    <div class="labels">
        {% for label in labels %}
            <div class="label small">
                <div class="left">
                    <div class="label-name">{{ label.name }}</div>
                    <div class="label-description">{{ label.description }}</div>
                </div>
                <div class="right">
                    <img class="label-image" src="data:image/png;base64,{{ label.image.data_b64 }}" />
                </div>
            </div>
        {% endfor %}
    </div>
{% endblock %}
