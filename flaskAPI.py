from flask import Flask,jsonify,request
from data import data

app = Flask(__name__)
@app.route("/")
def index():
    return jsonify({
        "data":data,
        "message":"success!"
    }),200

@app.route("/star")
def star():
    url = request.url
    url = url.split('/')[3].split('=')[1]
    url = url.replace('%20', ' ')
    url = url.replace('%5B', '[')
    url = url.replace('%5D', ']')
    print(url)

    star_data = [item for item in data if item["Star Name"] == url]
    return jsonify({
        "data": star_data,
        "status": "success"
    }), 200

if __name__ == "__main__":
    app.run()