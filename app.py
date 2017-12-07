#!flask/bin/python
from flask import Flask, jsonify

app = Flask(__name__)


temp = [
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
def get_temp():
    return jsonify({'temp': temp})

if __name__ == '__main__':
    app.run(debug=True)
