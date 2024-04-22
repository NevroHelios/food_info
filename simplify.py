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
        
        for nutriment in nutriment_list:
            dct[nutriment] = dct.get(nutriment, '0')
        
        dct = {key.title() : val for key, val in dct.items()}
        container['nutriments'] = dct
        
    elif facts == container["nutriscore_data"]:
        dct = {}
        for key in facts:
            if len(key.split('_')) != 1:
                if key.split('_')[0] == 'is':
                    dct[key.split('_')[1]] = facts[key]
                else:
                    dct[' '.join(key.split('_'))] = facts[key]
        dct['grade'] = facts['grade'] 
        dct = {key.title() : val for key, val in dct.items()}
        container["nutriscore_data"] = dct
    
    
nutriment_list = ["biotin",'bcaa','potassium', 'inositol', 'chloride', 'proteins', 'carbohydrates', 'galactose', 'creatine', 'oligosaccharide', 'glucose', 'erythritol', 'biotin', 'energy', 'fiber', 'water', 'taurine', 'starch', 'magnesium', 'molybdenum', 'fat', 'acidity', 'folates', 'carnitine', 'fructose', 'iron', 'choline', 'silica', 'iodine', 'sodium', 'manganese', 'cholesterol', 'casein', 'maltose', 'bcaa', 'calcium', 'alcohol', 'selenium', 'polydextrose', 'sulphate', 'phosphorus', 'caffeine', 'salt', 'copper', 'allulose', 'maltodextrins', 'cocoa', 'zinc', 'sucrose', 'chlorophyl', 'chromium', 'lactose', 'sugars', 'molybdenum', 'polydextrose']