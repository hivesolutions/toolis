{% extends "partials/simple.html.tpl" %}
{% block title %}Labels{% endblock %}
{% block content %}
    {% set count = label_groups|length %}
    {% set index = 0 %}
    <div class="labels print" data-delay="1000">
        {% for labels in label_groups %}
            {% set index = index + 1 %}
            <div class="page">
                <div class="page-counter">Page {{ index }} of {{ count }}</div>
                {% for label in labels %}
                    {% if label %}
                        <div class="label small">
                            <div class="left">
                                <div class="label-name">{{ label.name }}</div>
                                <div class="label-description">{{ label.description }}</div>
                            </div>
                            <div class="right">
                                <img class="label-image" src="data:image/png;base64,{{ label.image.data_b64 }}" />
                            </div>
                        </div>
                    {% endif %}
                {% endfor %}
            </div>
        {% endfor %}
    </div>
{% endblock %}
