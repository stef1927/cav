from django import template


register = template.Library()


@register.filter(name='addclass')
def addclass(value, arg):
    widget = value.field.widget
    args = widget.attrs.get('class') + ' ' + arg if widget.attrs.get('class') else arg
    return value.as_widget(attrs={'class': args})
