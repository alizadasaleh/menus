from django import template
from django.urls import reverse, NoReverseMatch
from ..models import MenuItem
from django.utils.safestring import mark_safe


register = template.Library()

def build_menu_html(request, menu_items):
    html = ''
    for item in menu_items:
        try:
            url = item.get_absolute_url()
        except NoReverseMatch:
            url = '#'

        active = 'active' if request.path == url else ''
        if item.children.exists():
            html += f'<li class="{active}"><a href="{url}">{item.title}</a>'
            html += '<ul>'
            html += build_menu_html(request, item.children.all())
            html += '</ul></li>'
        else:
            html += f'<li class="{active}"><a href="{url}">{item.title}</a></li>'

    return mark_safe(html) 

@register.simple_tag(takes_context=True)
def draw_menu(context, menu_name):
    request = context['request']
    root_items = MenuItem.objects.filter(menu_name=menu_name, parent__isnull=True).prefetch_related('children')
    menu_html = build_menu_html(request, root_items)
    return menu_html
