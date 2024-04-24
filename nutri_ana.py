# Edamam Nutrition Analysis

import requests

url = "https://edamam-edamam-nutrition-analysis.p.rapidapi.com/api/nutrition-data"


headers = {
	"X-RapidAPI-Key": "9e6b59345bmsh53d54fedfdaed90p1bcb61jsnfb94bdc3a78f",
	"X-RapidAPI-Host": "edamam-edamam-nutrition-analysis.p.rapidapi.com"
}

def get_labels(ingr, url=url, headers=headers):
    
    if ingr:
        
        querystring = {"ingr" : ingr, 
                    "nutrition-type" : "cooking"}
        response = requests.get(url, headers=headers, params=querystring)
        response =  response.json()
        labels = response['healthLabels']
        
        labels = [' '.join(label.split('_')) for label in labels]
        
        return labels
    
    return False


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