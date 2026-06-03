{% extends "layout.html" %}

{% block content %}

<div style="text-align:center; margin-bottom:40px;">
    <img src="/static/photo.jpg" alt="מרכז צעירים" style="width:220px;">
</div>

<h2>האזור האישי שלי</h2>

<p style="font-size:18px;">
    <strong>שם:</strong>
    {{ session.first_name }} {{ session.last_name }}
</p>

<p style="font-size:18px;">
    <strong>טלפון:</strong>
    {{ session.phone }}
</p>

<!-- כפתור התנתקות -->
<a href="/logout"
   style="
       position:fixed;
       bottom:25px;
       left:25px;
       padding:10px 22px;
       background:#d9534f;
       color:white;
       text-decoration:none;
       border-radius:8px;
       font-size:14px;
       font-weight:bold;
   ">
    התנתקות
</a>

{% endblock %}
