def to_camel_case(text):
    import re
    template = r'[_|-]\w'
    allresults = re.findall(template, text)
    for i in allresults:
        text = text.replace(i, i[1].upper())
    return text