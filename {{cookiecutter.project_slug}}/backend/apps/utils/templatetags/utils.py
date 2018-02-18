import re

from django import template
from django.conf import settings
from django.forms import ChoiceField, FileField, MultipleChoiceField
from django.utils.translation import get_language_info as dj_get_language_info

# TODO: write tests.

register = template.Library()


class SetVarNode(template.Node):
    def __init__(self, var_name, var_value):
        self.var_name = var_name
        self.var_value = var_value

    def render(self, context):
        try:
            value = template.Variable(self.var_value).resolve(context)
        except template.VariableDoesNotExist:
            value = ''

        context[self.var_name] = value
        return ''


# pylint: disable=unused-argument
@register.tag(name='set')
def set_var(parser, token):
    try:
        arg = token.contents.split(" ", 1)[1]
    except IndexError:
        raise template.TemplateSyntaxError('"set" tag requires arguments')

    match = re.search(r'(.*?) as (\w+)', arg)
    if not match:
        raise template.TemplateSyntaxError('"set" tag has invalid arguments')

    var_value, var_name = match.groups()
    return SetVarNode(var_name, var_value)


@register.simple_tag
def get_settings(name):
    if name in settings.ALLOWABLE_TEMPLATE_SETTINGS:
        return getattr(settings, name, '')
    return ''


@register.simple_tag(takes_context=True)
def build_absolute_url(context, location=None):
    request = context['request']
    return request.build_absolute_uri(location)


@register.simple_tag()
def get_language_info(lang_code):
    return dj_get_language_info(lang_code)


@register.simple_tag(takes_context=True)
def get_params_url(context, exclude=None):
    request = context['request']

    if exclude is not None:
        exclude = exclude.split(',')
    else:
        exclude = []

    params = []
    for key, value in sorted(request.GET.items()):
        if key in exclude:
            continue

        param = '{}={}'.format(key, value)
        params.append(param)

    url = '&'.join(params)
    return url


@register.filter(name='field_value')
def field_value(field):
    if field.form.is_bound:
        if isinstance(field.field, FileField) and field.data is None:
            val = field.form.initial.get(field.name, field.field.initial)
        else:
            val = field.data
    else:
        val = field.form.initial.get(field.name, field.field.initial)
        if callable(val):
            val = val()
    if val is None:
        val = ''
    return val


@register.filter(name='display_value')
def field_display_value(field):
    value = field_value(field)
    if isinstance(field.field, MultipleChoiceField):
        descriptions = []
        for (val, description) in field.field.choices:
            if str(val) in value:
                descriptions.append(description)
        if descriptions:
            return descriptions
    elif isinstance(field.field, ChoiceField):
        for (val, description) in field.field.choices:
            if str(val) == value:
                return description
    return value


@register.filter
def subtract(value, arg):
    return int(value) - int(arg)
