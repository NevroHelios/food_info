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
    product_info = api.product.get(code, fields=["code", "product_name", "image_url", "brands", "nutriscore_data", "nutriments", "ingredients_text_en"])
    
    # simplify the the nutrients
    nutri_simplify(product_info, product_info['nutriments'])
    nutri_simplify(product_info, product_info['nutriscore_data'])
    
    product_info['labels'] = get_labels("ingredients_text_en")
    product_info.pop("ingredients_text_en")
    
    return jsonify(product_info)
    

if __name__ == '__main__':
    app.run(debug=True)