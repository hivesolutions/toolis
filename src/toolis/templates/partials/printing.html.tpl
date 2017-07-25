{% extends "partials/base.html.tpl" %}
{% block body_class %}{{ super() }} printing{% endblock %}
{% block head %}
    {{ super() }}
    <link rel="stylesheet" type="text/css" href="//libs.bemisc.com/layout/css/layout.printing.css" />
{% endblock %}
{% block footer %}{% endblock %}
