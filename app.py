from flask import json
from flask import request
from flask import Flask

app = Flask(__name__)

@app.route('/')
def api_root():
    return 'welcome'

@app.route('/webhook/receiver',methods=['POST'])
def api_gitmsg():
    if request.headers['Content-Type'] ==   'application/json':
        return json.dumps(request.json)

if __name__ == '__main__':
    app.run(debug=True)