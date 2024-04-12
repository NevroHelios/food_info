import re

def nutri_simplify(container, facts):
    if facts == container['nutriments']:
        dct= {}
        for val in facts:
            if len(re.split(r"[_-]", val)) == 1:
                dct[val] = facts[val]
                perv = val
            if len(re.split(r"[_-]", val)) == 2 and val.split('_')[-1] == 'unit':
                dct[perv] = str(f"{dct[perv]} ") + facts[val] 
        
        dct['energy'] = str(round(int(dct['energy'].split()[0]) * 0.239006)) + " Kcal"
        container['nutriments'] = dct
        
    elif facts == container["nutriscore_data"]:
        dct = {}
        for key in facts:
            if len(key.split('_')) != 1 and key != 'grade':
                dct[key] = facts[key]
        container["nutriscore_data"] = dct
    