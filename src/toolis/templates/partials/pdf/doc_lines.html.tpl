{% extends "partials/pdf/doc_head.html.tpl" %}
{% block header_extra %}
    {{ super() }}
    <div class="small-separator">&nbsp;</div>
    <table class="table-contents">
        <thead>
            {% block lines_header %}{% endblock %}
        </thead>
    </table>
{% endblock %}
{% block footer %}
    {{ super() }}
    <div class="line-footer">&nbsp;</div>
    <table class="table-footer">
        <tr>
            <td class="table-footer-vat">
                <table class="table-vat">
                    <thead class="table-values-header">
                        <tr>
                            <th align="left">TAX</th>
                            <th align="right">VALUE</th>
                        </tr>
                    </thead>
                    <tbody>
                        {% for item in operation.vat_list %}
                            <tr>
                                <td align="left">{{ item.vat_rate_s }} %</td>
                                <td align="right">{{ item.vat_s }} €</td>
                            </tr>
                        {% endfor %}
                        <tr>
                            <td align="left">Total</td>
                            <td align="right">{{ operation.vat_s }} €</td>
                        </tr>
                    </tbody>
                </table>
            </td>
            <td width="140"></td>
            <td class="totals">
                <table class="table-totals">
                    {% if operation.type == 1 %}
                        <tr>
                            <td class="table-totals-left" align="left">VAT</td>
                            <td align="right">{{ operation.vat_s }} €</td>
                        </tr>
                        <tr>
                            <td class="table-totals-left" align="left">SUBTOTAL</td>
                            <td align="right">{{ operation.subtotal_s }} €</td>
                        </tr>
                        <tr>
                            <td class="table-totals-left" align="left">DISCOUNT</td>
                            <td align="right">{{ operation.discount_vat_s }} €</td>
                        </tr>
                    {% elif operation.type == 2 %}
                        <tr>
                            <td class="table-totals-left" align="left">DISCOUNT</td>
                            <td align="right">{{ operation.discount_s }} €</td>
                        </tr>
                        <tr>
                            <td class="table-totals-left" align="left">SUBTOTAL</td>
                            <td align="right">{{ operation.subtotal_s }} €</td>
                        </tr>
                        <tr>
                            <td class="table-totals-left" align="left">VAT</td>
                            <td align="right">{{ operation.vat_s }} €</td>
                        </tr>
                    {% endif %}
                    <tr class="table-totals-empty">
                        <td>&nbsp;</td>
                        <td>&nbsp;</td>
                    </tr>
                    <tr>
                        <td class="table-totals-left table-totals-total" align="left">TOTAL</td>
                        <td class="table-totals-total" align="right">{{ operation.price_vat_s }} €</td>
                    </tr>
                </table>
            </td>
        </tr>
    </table>
    <div class="large-separator">&nbsp;</div>
    <div class="ender">
        <table>
            <tr>
                {% if document.digest_chunk %}
                    <td align="left">{{ document.digest_chunk }} - Processed by certified application nr. 1024/AT</td>
                {% else %}
                    <td align="left">Processed by certified application nr. 1024/AT</td>
                {% endif %}
                <td align="right"><span class="strong">TAKE THE BILL - &copy; Copyright Hive Solutions Lda.</span></td>
            </tr>
        </table>
    </div>
{% endblock %}
{% block content %}
    {{ super() }}
    <div>
        <div class="large-separator">&nbsp;</div>
        <table class="table-contents">
            <thead>
                {{ self.lines_header() }}
            </thead>
            <tbody>
                {% block lines %}{% endblock %}
            </tbody>
        </table>
        <div class="min-separator">&nbsp;</div>
        <div class="line-footer">&nbsp;</div>
        <div class="min-separator">&nbsp;</div>
        {% if document.metadata.notes or config.advice %}
            <div class="observations">
                <div class="observations-title">OBSERVATIONS</div>
                <div class="min-separator">&nbsp;</div>
                <div class="observations-contents">
                    {% if document.metadata.notes %}
                        <div>{{ document.metadata.notes|nl_to_br }}</div>
                    {% endif %}
                    {% if config.advice %}
                        <div>The merchandise has been put at customer's disposition at the current date.</div>
                    {% endif %}
                </div>
            </div>
            <div class="min-separator">&nbsp;</div>
            <div class="line-footer">&nbsp;</div>
        {% endif %}
    </div>
{% endblock %}
