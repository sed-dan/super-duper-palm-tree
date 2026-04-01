from django import template
import re

register = template.Library()



@register.filter
def censor(value):
    bwdict = ["badword", "архитектура"]
    for word in bwdict:
        # \b - граница слова, re.IGNORECASE - игнорировать регистр
        pattern = r'\b' + re.escape(word) + r'\b'
        value = re.sub(pattern, word[0] + '*' * (len(word)-1), value, flags=re.IGNORECASE)
    return value

