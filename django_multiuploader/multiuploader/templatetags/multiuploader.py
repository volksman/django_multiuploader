from django import template
from django.conf import settings

register = template.Library()

@register.simple_tag()
def multiupform(value):
    try:
        app, model = value.split('.')
    except:
        raise ValueError('Value should be an app.model name')

    t = template.loader.select_template(['multiuploader/%s_%s.html' % (app, model), 'multiuploader/base.html'])
    c = template.Context({ 'STATIC_URL':settings.STATIC_URL, 'model': model })

    return t.render(c)
