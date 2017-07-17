{% extends "partials/pdf/doc.html.tpl" %}
{% set operation = document.payload.operation %}
{% set system_company = document.payload.system_company %}
{% set customer = operation.customer %}
{% block content %}
    {{ super() }}
    <table class="table-header">
        <tr>
            <td class="sender">
                {% set address = system_company.primary_address %}
                {% set contact_information = system_company.primary_contact_information %}
                <div class="sender-title">{{ system_company.name|default('Anonymous', true) }}</div>
                <div>{{ address.street_name|default('', true) }}</div>
                <div>{{ address.zip_code|default('', true) }} {{ address.zip_code_name|default('', true) }}</div>
                <div>Telephone - {{ contact_information.phone_number|default('N/A', true) }}</div>
                <div>Tax Number - {{ system_company.tax_number|default('N/A', true) }}</div>
                <div>{{ system_company.corporate_registration_entity }}</div>
            </td>
            <td width="140"></td>
            <td class="receiver">
                {% if customer %}
                    {% set address = customer.primary_address %}
                    {% set contact_information = customer.primary_contact_information %}
                    <div class="receiver-title">{{ customer.representation|default('Anonymous', true) }}</div>
                    <div>{{ address.street_name|default('', true) }}</div>
                    <div>{{ address.zip_code|default('', true) }} {{ address.zip_code_name|default('', true) }}</div>
                    {% if contact_information.phone_number %}
                        <div>Telephone - {{ contact_information.phone_number }}</div>
                    {% endif %}
                    {% if customer.tax_number %}
                        <div>Tax Number - {{ customer.tax_number }}</div>
                    {% endif %}
                {% else %}
                    <div class="receiver-title">Anonymous</div>
                {% endif %}
            </td>
        </tr>
    </table>
    <table class="table-notes">
        <tr>
            <td class="table-notes-cell" width="100%">
                <div class="table-notes-header">Identifier</div>
                <div>{{ document.identifier }}</div>
            </td>
            <td width="20">&nbsp;</td>
            <td class="table-notes-cell" width="100%">
                <div class="table-notes-header">Issue Date</div>
                <div>{{ date_time(document.issue_date|default('N/A', true), '%d %B %Y') }}</div>
            </td>
            <td width="20">&nbsp;</td>
            <td class="table-notes-cell" width="100%">
                <div class="table-notes-header">Due Date</div>
                <div>{{ date_time(document.due_date|default(document.issue_date|default('N/A', true)), '%d %B %Y') }}</div>
            </td>
        </tr>
    </table>
{% endblock %}
