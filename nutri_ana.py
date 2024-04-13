import requests

url = "https://edamam-edamam-nutrition-analysis.p.rapidapi.com/api/nutrition-data"


headers = {
	"X-RapidAPI-Key": "9e6b59345bmsh53d54fedfdaed90p1bcb61jsnfb94bdc3a78f",
	"X-RapidAPI-Host": "edamam-edamam-nutrition-analysis.p.rapidapi.com"
}

def get_labels(ingr, url=url, headers=headers):
    
    querystring = {"ingr" : ingr, 
                   "nutrition-type" : "cooking"}
    response = requests.get(url, headers=headers, params=querystring)
    response =  response.json()
    return response['healthLabels']