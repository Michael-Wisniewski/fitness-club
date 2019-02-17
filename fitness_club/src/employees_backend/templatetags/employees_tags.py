from django import template
from account.models import User

register = template.Library()

@register.inclusion_tag('employees_backend/tags_templates/employees_shortcut.html')
def employees_shortcut():
    employees = User.objects.filter(is_employee=True)[:3]
    return {'employees': employees}