from flask import Flask, request, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route('/', methods=['GET','POST'])
def index():
    if request.method=="GET":
        return {'res':'ok'}
    else:
        name=request.json['name']
        return {'name':name}
    

if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port=3009)
