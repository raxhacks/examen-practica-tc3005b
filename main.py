from flask import Flask, jsonify
import pandas as pd

app = Flask(__name__)

@app.route('/')
def csv_to_json():
    df = pd.read_csv('mx.csv')
    data = df.to_dict(orient='records')
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)