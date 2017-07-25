{% extends "partials/printing.html.tpl" %}
{% block title %}Labels Large{% endblock %}
{% block content %}
    <div class="labels print" data-delay="1000">
        {% for labels in label_groups %}
            <div class="page">
                <div class="page-counter">Page {{ loop.index }} of {{ label_groups|length }}</div>
                {% for label in labels %}
                    {% if label %}
                        <div class="label large">
                            <img class="label-image" src="data:image/png;base64,{{ label.image.data_b64 }}" />
                            <div class="label-name">{{ label.name }}</div>
                            <div class="label-description">{{ label.description }}</div>
                        </div>
                    {% endif %}
                {% endfor %}
            </div>
        {% endfor %}
    </div>
{% endblock %}
