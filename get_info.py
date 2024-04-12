from flask import Flask, request, jsonify
import re
import openfoodfacts
from simplify import simplify


app = Flask(__name__)

@app.route('/product_info', methods=['POST'])
def get_product_info():
    data = request.get_json(force=True)
    code = data['code']
    api = openfoodfacts.API(user_agent="MyAwesomeApp/1.0")
    product_info = api.product.get(code, fields=["code", "product_name", "image_url", "brands", "brands_tags", "nutriscore_data", "nutriments"])
    
    product_info['nutriments'] = simplify(product_info, product_info['nutriments'])
    
    return jsonify(product_info)
    

if __name__ == '__main__':
    app.run(debug=True)