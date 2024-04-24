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
    
    
    product_info = api.product.get(code, fields=["code", "product_name", "image_url", "brands", "nutriscore_data", "nutriments", "ingredients_text_en", "nutrient_levels", "nutri_score"])
    
    if product_info == None:
        return jsonify({"product_name" : "NO INFO FOUND"})
    
    # simplify the the nutrients
    try:
        nutri_simplify(product_info, product_info['nutriments'])
    except:
        pass
    
    try:
        nutri_simplify(product_info, product_info['nutriscore_data'])
    except:
        pass
    
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