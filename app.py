# import Flask, render_template, jsonify
from flask import Flask, render_template, jsonify
# import Pictures
from pictures_data import Pictures

# create Flask app
app = Flask(__name__)



# --- API Routes ---
@app.route('/api/pictures')
def pictures():
    return jsonify(Pictures)

@app.route('/api/pictures/<country>')
def picture_country(country):
    p = list(filter(lambda p: p['country'].lower() == country.lower(), Pictures))
    return jsonify(p)

@app.route('/api/pictures/<int:id>')
def picture_int(id):
    for p in Pictures:
        if p['id'] == id:
            return jsonify(p)


# --- HTML Routes ---
@app.route('/pictures')
def pictures_index():
    return render_template('pictures_index.html', pictures = Pictures)

@app.route('/pictures/<int:id>')
def pictures_id(id):
    p = list(filter(lambda p: p['id']==id, Pictures))
    return render_template('pictures_index.html', pictures = p)

@app.route('/pictures/<country>')
def picture_by_country(country):
    p = list(filter(lambda p: p['country'].lower() == country.lower(), Pictures))
    return render_template('pictures_index.html', pictures=p)

# run our Flask app
if __name__ == '__main__':
    app.run(debug=True)
