#!flask/bin/python
from flask import Flask, jsonify, abort

app = Flask(__name__)

temps = [
    {
        'type': 'F',
        'title': 32,
        'description': 'Farenheit'
    },
    {
        'type': 'C',
        'title': 0,
        'description': 'Celcius'
    }
]


@app.route('/todo/api/v1.0/temp', methods=['GET'])
def get_temps():
    return jsonify({'temp': temps})


@app.route( '/todo/api/v1.0/temp/<type>', methods=['GET'])
def get_temp(type):
    temp = [temp for temp in temps if temp['type'] == type]
    if len(temp) == 0:
        abort(404)
    return jsonify({'task': temp[0]})

if __name__ == '__main__':
    app.run(debug=True)
