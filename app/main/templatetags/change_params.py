"""Шаблонний тег для зміни параметрів GET запроса"""


from django.template import Library
from django.utils.http import urlencode


register = Library()


@register.simple_tag(takes_context=True)
def change_params(context: dict, **kwargs):
    result = context["request"].GET.dict()
    result.update(kwargs) 
    return urlencode(result)
