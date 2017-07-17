<html>
    <head>
        {% include "partials/pdf/style.html.tpl" %}
    </head>
    <body>
        <div id="header">
            {% block header %}{% endblock %}
        </div>
        <div id="header-extra">
            {% block header_extra %}{% endblock %}
        </div>
        <div id="footer">
            {% block footer %}{% endblock %}
        </div>
        <div id="content">
            <pdf:nexttemplate name="extra" />
            {% block content %}{% endblock %}
        </div>
    </body>
</html>
