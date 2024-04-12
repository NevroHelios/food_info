import re

def simplify(container, facts):
    dct= {}
    for val in facts:
        if len(re.split(r"[_-]", val)) == 1:
            dct[val] = facts[val]
        if len(re.split(r"[_-]", val)) == 2 and val.split('_')[-1] == 'unit':
            dct[val] = facts[val]
    return dct