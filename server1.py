from flask import Flask, jsonify, request, abort
from CountryDAO import countryDAO

app = Flask(__name__, static_url_path='', static_folder='.')

#app = Flask(__name__)

@app.route('/')
def index():
    return "Hello, World!"

#curl "http://127.0.0.1:5000/books"
@app.route('/Countrys')
def getAll():
    #print("in getall")
    results = countryDAO.getAll()
    return jsonify(results)

@app.route('/regionInfo')
def findByRegion():
    #print("in getall")
    return "FindByRegion"
    results = countryDAO.findByRegion()
    return jsonify(results)


#curl "http://127.0.0.1:5000/books/2"
@app.route('/Countrys/<int:id>')
def findById(id):
    foundCountry = countryDAO.findByID(id)

    return jsonify(foundCountry)

@app.route('/Countrys/<country_name>', methods=['GET'])
def findByCountry(country_name):
    foundCountry = countryDAO.findByCountry(country_name)

    return jsonify(foundCountry)


#curl  -i -H "Content-Type:application/json" -X POST -d "{\"title\":\"hello\",\"author\":\"someone\",\"price\":123}" http://127.0.0.1:5000/books
@app.route('/Countrys', methods=['POST'])
def create():
    
    if not request.json:
        abort(400)
    # other checking 
    Country = {
        "country": request.json['country'],
        "Land_area": request.json['Land_area'],
        "capital": request.json['capital'],
        "co2": request.json['co2'],
        "C_Code": request.json['C_Code'],
        "Life_ex": request.json['Life_ex'],
        "Min_Wage": request.json['Min_Wage'],
        "Off_language": request.json['Off_language'],
        "Population": request.json['Population'],
        "Lat": request.json['Lat'],
        "lon": request.json['lon']
    }
    values =(Country['country'],Country['Land_area'],Country['capital'],Country['co2'],Country['C_Code'],Country['Life_ex'],Country['Min_Wage'],Country['Off_language'],Country['Population'],Country['Lat'],Country['lon'])
    newId = countryDAO.create(values)
    Country['id'] = newId
    return jsonify(Country)

#curl  -i -H "Content-Type:application/json" -X PUT -d "{\"title\":\"hello\",\"author\":\"someone\",\"price\":123}" http://127.0.0.1:5000/books/1
@app.route('/Countrys/<int:id>', methods=['PUT'])
def update(id):
    foundCountrys = countryDAO.findByID(id)
    if not foundCountrys:
        abort(404)
    
    if not request.json:
        abort(400)
    reqJson = request.json
    if 'Land_area' in reqJson and type(reqJson['Land_area']) is not int:
        abort(400)
    if 'Life_ex' in reqJson and type(reqJson['Life_ex']) is not float:
        abort(400)
    if 'Population' in reqJson and type(reqJson['Population']) is not int:
        abort(400)
    if 'Lat' in reqJson and type(reqJson['Lat']) is not float:
        abort(400)
    if 'lon' in reqJson and type(reqJson['lon']) is not float:
        abort(400)

    if 'country' in reqJson:
        foundCountrys['country'] = reqJson['country']
    if 'Land_area' in reqJson:
        foundCountrys['Land_area'] = reqJson['Land_area']
    if 'capital' in reqJson:
        foundCountrys['capital'] = reqJson['capital']
    if 'co2' in reqJson:
        foundCountrys['co2'] = reqJson['co2']
    if 'C_Code' in reqJson:
        foundCountrys['C_Code'] = reqJson['C_Code']
    if 'Life_ex' in reqJson:
        foundCountrys['Life_ex'] = reqJson['Life_ex']
    if 'Min_Wage' in reqJson:
        foundCountrys['Min_Wage'] = reqJson['Min_Wage']
    if 'Off_language' in reqJson:
        foundCountrys['Off_language'] = reqJson['Off_language']
    if 'Population' in reqJson:
        foundCountrys['Population'] = reqJson['Population']
    if 'Lat' in reqJson:
        foundCountrys['Lat'] = reqJson['Lat']
    if 'lon' in reqJson:
        foundCountrys['lon'] = reqJson['lon']
    values = (foundCountrys['country'],foundCountrys['Land_area'],foundCountrys['capital'],foundCountrys['co2'],foundCountrys['C_Code'],foundCountrys['Life_ex'],foundCountrys['Min_Wage'],foundCountrys['Off_language'],foundCountrys['Population'],foundCountrys['Lat'],foundCountrys['lon'],foundCountrys['id'])
    countryDAO.update(values)
    return jsonify(foundCountrys)
        

    

@app.route('/Countrys/<int:id>' , methods=['DELETE'])
def delete(id):
    countryDAO.delete(id)
    return jsonify({"done":True})




if __name__ == '__main__' :
    app.run(debug= True)