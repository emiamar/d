import models
import serializer
from base.views import GenericAPIView

{% for endpoint in endpoints %}


locals()['{{endpoint.name}}'] = type(
    '{{endpoint.name}}',
    (GenericAPIView,),
    {
        'serializer': getattr(serializer, '{{endpoint.serializer_object.name}}'),
        'queryset': getattr(models, '{{endpoint.queryset.model.name}}').{{endpoint.queryset.query_method | safe}},
        {% if endpoint.queryset.queryset_type == 'LIST'%}
        'many': True,
        {% endif %}
    }
)
{% endfor %}
