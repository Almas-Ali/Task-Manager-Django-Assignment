from django import template

register = template.Library()


@register.filter(name="priority_mode")
def priority_mode(value: str):
    """Return the priority mode"""
    if value == "1":
        return "LOW"
    elif value == "2":
        return "MEDIUM"
    return "HIGH"
