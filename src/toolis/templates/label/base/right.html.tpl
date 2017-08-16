{% extends "partials/printing.html.tpl" %}
{% block content %}
    <div class="labels print" data-delay="1000">
        {% for labels in label_groups %}
            <div class="page">
                <div class="page-counter">Page {{ loop.index }} of {{ label_groups|length }}</div>
                {% for label in labels %}
                    {% if label %}
                        <div class="{% block label_cls %}label label-right{% endblock %}">
                            <div class="left">
                                <img class="label-image" src="data:{{ label.image.mime }};base64,{{ label.image.data_b64 }}" />
                            </div>
                            <div class="right">
                                <div class="label-code">{{ label.code }}</div>
                                <div class="label-name">{{ label.name }}</div>
                                <div class="label-description">{{ label.description }}</div>
                            </div>
                        </div>
                    {% endif %}
                {% endfor %}
            </div>
        {% endfor %}
    </div>
{% endblock %}
