from flask import Flask, render_template, request, jsonify
import requests
from pictures_data import Pictures

app = Flask(__name__)

@app.route('/pictures')
def pictures_index():
    pictures = requests.get('http://localhost:5000/api/pictures')
    pictures_json = pictures.json()
    return render_template('pictures_index.html', pictures=pictures_json)

@app.route('/pictures/<int:id>')
def pictures_show(id):
    pictures = requests.get('http://localhost:5000/api/pictures/'+ str(id))
    pictures_json = pictures.json()
    return render_template('picture_show.html', picture=pictures_json)

@app.route('/pictures/<country>')
def pictures_list_by_country(country):
    pictures = requests.get('http://localhost:5000/api/pictures/'+ country)
    pictures_json = pictures.json()
    return render_template('pictures_index.html', pictures=pictures_json)

# --- API Routes ---

@app.route('/api/pictures')
def all_pictures():
    return jsonify(Pictures)

@app.route('/api/pictures/<country>')
def pictures_by_country(country):
    return jsonify([picture for picture in Pictures if picture["country"].lower() == country.lower()])

@app.route('/api/pictures/<int:id>')
def one_picture(id):
    if request.method == 'POST':
        print(params)
    picture = next(picture for picture in Pictures if picture["id"] == id)
    return jsonify(picture)

app.run(debug=True)
