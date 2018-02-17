from __future__ import unicode_literals

from django.db import models

import methods

{% for model in model_objects %}

{{model.name}}Dict = {
        '__module__': '{{model.app.name_lower}}',
    {% for field in model.modelfield_set.all %}
        '{{field.name}}': models.{{field.get_field_type_display}}({% include 'modeller/attributes.py' %}),
    {% endfor %}
}

for name, cls in methods.{{model.name|lower}}.__dict__.items():
    if callable(cls):
        {{model.name}}Dict[name] = cls

{{model.name}} = type(
    str('{{model.name}}'),
    (models.Model,),
    {{model.name}}Dict
)

{% endfor %}