from django import template 
from django.utils.html import escape, mark_safe
register = template.Library() 
@register.filter 
def first_letters(iterable):
    result = "" 
    for item in iterable:
        result += item[0] 
    return result 


@register.filter(name="nth_letters", is_safe=True) 
def other_letters(iterable, num):
    result = "" 
    for item in iterable:
        if len(item) < num or not item[num - 1].isalpha(): result += " " 
        else: result += item[num -1] 
    return result 

@register.simple_tag
def mute(*args):
    return ""

@register.simple_tag
def make_ul(iterable):
    content = ["<ul>"]
    for item in iterable:
        content.append(f"<li>{escape(item)}</li>")
    content.append("</ul>")
    content = "".join(content)
    return mark_safe(content)