from flask import Flask, render_template, jsonify, request
from advertiser.advertiser import Advertiser

app = Flask(__name__)

advert = Advertiser()


@app.route("/api/")
def main():
    return render_template('index.html')


@app.route("/api/advertiser", methods=['GET'])
def test_json():
    return jsonify({'request': 'advertiser/name/'})


@app.route("/api/advertiser", methods=['POST'])
def add_advertiser():
    if request.method == 'POST':
        name = request.json.get('name')
        contact = request.json.get('contact')
        credit_limit = request.json.get('credit_limit')
        try:
            if advert.get(name):
                return jsonify({'error': 'Advertiser already exists'})
        except Exception as e:
            return jsonify({'error': 'error searching for possible reference'})
        if not name or not contact or not credit_limit:
            return jsonify({'error': 'All fields required'})
        advert.add(name, contact, credit_limit)
        return jsonify({'success': '{0} saved.'.format(name)})
    return jsonify({'error': 'No data supplied'})


@app.route("/api/advertiser/<name>", methods=['GET', 'PUT', 'DELETE'])
def get_advertiser(name):
    if request.method == 'GET':
        try:
            data = advert.get(name)
        except Exception as e:
            print e
            return jsonify({'error': '{0}'.format(e)})
        print data
        return jsonify(data)
    if request.method == 'DELETE':
        try:
            advert.delete(name)
        except Exception as e:
            return jsonify({'error': '{0}'.format(e)})
        return jsonify({'success': 'Advertiser {0} deleted'.format(name)})

if __name__ == "__main__":
    app.run()
