from flask import Flask, request, jsonify
import openfoodfacts

app = Flask(__name__)

@app.route('/product_info', methods=['POST'])
def get_product_info():
    data = request.get_json(force=True)
    code = data['code']
    api = openfoodfacts.API(user_agent="MyAwesomeApp/1.0")
    product_info = api.product.get(code, fields=["code", "product_name", "image_url", "brands", "brands_tags"])
    return jsonify(product_info)
    

if __name__ == '__main__':
    app.run(debug=True)