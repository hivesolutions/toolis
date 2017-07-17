{% extends "partials/pdf/layout.html.tpl" %}
{% block header %}
    {{ super() }}
    <table>
        <tr>
            <td align="left">
                {% if logo %}
                    <img src="data:image/png;base64,{{ logo }}" height="50" />
                {% endif %}
            </td>
            <td align="right">
                <div class="header-title">{{ name|locale }} - {{ document.identifier }}</div>
                <div class="header-page">
                    <div class="paging">
                        Page <pdf:pagenumber /> of <pdf:pagecount />
                    </div>
                </div>
            </td>
        </tr>
    </table>
{% endblock %}
{% block header_extra %}
    {{ super() }}
    <table>
        <tr>
            <td align="left">
                {% if logo %}
                    <img src="data:image/png;base64,{{ logo }}" height="50" />
                {% endif %}
            </td>
            <td align="right">
                <div class="header-title">{{ name|locale }} - {{ document.identifier }}</div>
                <div class="header-page">
                    <div class="paging">
                        Page <pdf:pagenumber /> of <pdf:pagecount />
                    </div>
                </div>
            </td>
        </tr>
    </table>
{% endblock %}
