from flask import Flask, render_template, jsonify, request, abort
from flask.ext.api import status
from advertiser.advertiser import Advertiser

app = Flask(__name__)

advert = Advertiser()


@app.route("/api/")
def main():
    return render_template('index.html')


@app.route("/api/advertiser/", methods=['GET'])
def get_advertiser_none():
    if request.method == 'GET':
        return jsonify({'request': 'advertiser/name/'})


@app.route("/api/advertiser/", methods=['POST'])
def add_advertiser():
    if request.method == 'POST':
        name = request.json.get('name')
        contact = request.json.get('contact')
        credit_limit = request.json.get('credit_limit')
        try:
            if advert.get(name):
                return (jsonify({'error': 'Advertiser already exists'}),
                        status.HTTP_409_CONFLICT)
        except Exception as e:
            return (jsonify({'error':
                             'error searching for possible reference'}),
                    status.HTTP_404_NOT_FOUND)
        if not name or not contact or not credit_limit:
            return (jsonify({'error': 'All fields required'}),
                    status.HTTP_400_BAD_REQUEST)
        advert.add(name, contact, credit_limit)
        return jsonify({'success': '{0} saved.'.format(name)})
    return (jsonify({'error': 'No data supplied'}),
            status.HTTP_400_BAD_REQUEST)


@app.route("/api/advertiser/<name>", methods=['PUT', 'DELETE'])
def get_advertiser(name):
    if request.method == 'PUT':
        return jsonify({'error': 'Not yet implemented'})
    if request.method == 'DELETE':
        try:
            advert.delete(name)
        except Exception as e:
            abort(400)
            return jsonify({'error': '{0}'.format(e)})
        return jsonify({'success': 'Advertiser {0} deleted'.format(name)})

if __name__ == "__main__":
    app.run()
