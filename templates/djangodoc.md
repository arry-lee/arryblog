{% extends "admin/base.html" %}
{% load i18n %}

{% block extrahead %}
<style type="text/css">
.module table { width:100%; }
.module table p { padding: 0; margin: 0; }
</style>
{% endblock %}

{% block content %}
{% for model in models|dictsort:'name'%}
<div id="content-main">
<h2 id="{{ model.name }}">{{ model.name }}<small>{{ model.summary }}</small></h2>

{{ model.description }}

<h3>{% trans '数据表' %}{{forloop.counter}}</h3>
<div class="module">
<table class="model">
<thead>
<tr>
    <th>{% trans 'Field' %}</th>
    <th>{% trans 'Type' %}</th>
    <th>{% trans 'Description' %}</th>
</tr>
</thead>
<tbody>
{% for field in model.fields|dictsort:"name" %}
<tr>
    <td>{{ field.name }}</td>
    <td>{{ field.data_type }}</td>
    <td>{{ field.verbose }}{% if field.help_text %} - {{ field.help_text|safe }}{% endif %}</td>
</tr>
{% endfor %}
</tbody>
</table>
</div>

{% if model.methods %}
<h3>{% trans 'Methods with arguments' %}</h3>
<div class="module">
<table class="model">
<thead>
<tr>
    <th>{% trans 'Method' %}</th>
    <th>{% trans 'Arguments' %}</th>
    <th>{% trans 'Description' %}</th>
</tr>
</thead>
<tbody>
{% for method in model.methods|dictsort:"name" %}
<tr>
    <td>{{ method.name }}</td>
    <td>{{ method.arguments }}</td>
    <td>{{ method.verbose }}</td>
</tr>
{% endfor %}
</tbody>
</table>
</div>
{% endif %}

</div>
{% endfor %}
{% endblock %}