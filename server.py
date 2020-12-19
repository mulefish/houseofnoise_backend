from flask import Flask
from flask import jsonify
from flask import render_template
from flask_mongoengine import MongoEngine
app = Flask(__name__)




@app.route('/')
def root():
    print("root")
    message = "https://www.mongodb.com/try/download/community https://docs.mongodb.com/manual/tutorial/install-mongodb-on-os-x/#run-mongodb-community-edition "
    return render_template('index.html', message=message)

@app.route('/json')
def json(): 
    print("json path")
    result = {}
    result["hello"] = "world"
    return jsonify(result)

if __name__ == '__main__':
    app.run()