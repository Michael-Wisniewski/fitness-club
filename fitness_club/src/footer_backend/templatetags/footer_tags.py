from django import template

register = template.Library()

@register.inclusion_tag('footer_backend/tags_templates/footer_content_shortcut.html')
def footer_content_shortcut():
    data = {}
    data_file = open("/fitness_club/src/footer_backend/data.txt")

    for line in data_file:
        line_arr = line.split(" ", 1)
        if len(line_arr) > 1:
            data[line_arr[0]] = line_arr[1]

    data_file.close()

    return {'data': data}