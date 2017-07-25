{% extends "partials/simple.html.tpl" %}
{% block title %}Labels{% endblock %}
{% block content %}
    <div class="labels print" data-delay="1000">
        {% for label in labels %}
            <div class="label large">
            	<img class="label-image" src="data:image/png;base64,{{ label.image.data_b64 }}" />
                <div class="label-name">{{ label.name }}</div>
                <div class="label-description">{{ label.description }}</div>
            </div>
        {% endfor %}
    </div>
{% endblock %}
