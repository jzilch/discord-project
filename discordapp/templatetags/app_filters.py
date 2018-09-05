from django import template

register = template.Library()

@register.filter(name="format_youtube_url")
def format_youtube_url(value):
    ''' receives youtube url and formats it for iframe tags '''

    # replace "watch?v=" with "embed/"
    value = value[:value.find("watch?v=")] + "embed/" + value[value.find("watch?v=") + 8:]

    return value