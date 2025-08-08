from django import template
register = template.Library()


@register.simple_tag
def num_range(start, end):
    return range(int(start), int(end) + 1)


@register.filter
def filled(avg, index):
    try:
        return float(avg) >= int(index)
    except (TypeError, ValueError):
        return False
