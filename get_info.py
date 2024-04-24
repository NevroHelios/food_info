from flask import Flask, request, jsonify
import openfoodfacts
from simplify import nutri_simplify
from nutri_ana import get_labels


app = Flask(__name__)


@app.route('/product_info', methods=['POST'])
def get_product_info():
    data = request.get_json(force=True)
    code = data['code']
    api = openfoodfacts.API(user_agent="MyAwesomeApp/1.0")
    
    
    get_product_info = api.product.get(code, fields=["code", "product_name", "image_url", "brands", "nutriscore_data", "nutriments", "ingredients_text_en", "nutrient_levels", "nutri_score"])
    
    if get_product_info == None:
        # return jsonify({"product_name" : "NO INFO FOUND"})
        product_info = {
    "brands": "-",
    "code": "--",
    "image_url": "--",
    "labels": [
        'Not Found'
    ],
    "nutrient_levels": {
        "fat": "-",
        "salt": "-",
        "saturated-fat": "-",
        "sugars": "-"
    },
    "nutriments": {
        "alcohol": "0",
        "caffeine": "0",
        "calcium": "0",
        "carbohydrates": "0",
        "carnitine": "0",
        "chloride": "0",
        "cholesterol": "0",
        "cocoa": "0",
        "copper": "0",
        "energy": "0",
        "fat": "0",
        "fiber": "0",
        "fructose": "0",
        "glucose": "0",
        "inositol": "0",
        "iron": "0",
        "lactose": "0",
        "manganese": "0",
        "potassium": "0",
        "proteins": "0",
        "salt": "0",
        "sodium": "0",
        "starch": "0",
        "sucrose": "0",
        "sugars": "0"
    },
    "nutriscore_data": {
        "Beverage": 0,
        "Cheese": 0,
        "Energy Points": 0,
        "Energy Value": 0,
        "Fat": 0,
        "Fiber Points": 0,
        "Fiber Value": 0,
        "Fruits Vegetables Nuts Colza Walnut Olive Oils": 0,
        "Fruits Vegetables Nuts Colza Walnut Olive Oils Points": 0,
        "Fruits Vegetables Nuts Colza Walnut Olive Oils Value": 0,
        "Grade": "0",
        "Negative Points": 0,
        "Positive Points": 0,
        "Proteins Points": 0,
        "Proteins Value": 0,
        "Saturated Fat": 0,
        "Saturated Fat Points": 0,
        "Saturated Fat Value": 0,
        "Sodium Points": 0,
        "Sodium Value": 0,
        "Sugars Points": 0,
        "Sugars Value": 0,
        "Water": 0
    },
    "product_name": "-"
}
        return jsonify(product_info) 
    else:
        product_info = get_product_info
    
    # simplify the the nutrients
    try:
        nutri_simplify(product_info, product_info['nutriments'])
    except:
        product_info['nutriments'] = 'Error in Nutrition Information'
    
    try:
        nutri_simplify(product_info, product_info['nutriscore_data'])
    except:
        product_info['nutriscore_data'] = 'Error in  Nutri-Score Data'
    
    try:
        product_info['labels'] = get_labels("ingredients_text_en")
    except:
        pass
    # product_info['labels'] = [ "LOW_SUGAR", "VEGAN", "VEGETARIAN", "PESCATARIAN", "PALEO", "SPECIFIC_CARBS", "DAIRY_FREE", "GLUTEN_FREE", "WHEAT_FREE", "EGG_FREE", "MILK_FREE", "PEANUT_FREE", "TREE_NUT_FREE", "SOY_FREE", "FISH_FREE", "SHELLFISH_FREE", "PORK_FREE", "RED_MEAT_FREE", "CRUSTACEAN_FREE", "CELERY_FREE", "MUSTARD_FREE", "SESAME_FREE", "LUPINE_FREE", "MOLLUSK_FREE", "ALCOHOL_FREE", "NO_OIL_ADDED", "NO_SUGAR_ADDED", "FODMAP_FREE", "KOSHER"]
    
    try:
        product_info.pop("ingredients_text_en")
    except:
        pass
    
    return jsonify(product_info)
    

if __name__ == '__main__':
    app.run(debug=True)
    
    
    
    
