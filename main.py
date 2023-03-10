from flask import *
import requests 

app = Flask(__name__)

@app.route('/' , methods=['GET'])
def home_erre():
    return "please  put your  facebook  video url first"


@app.route('/url/' , methods=['GET'])
def home():
    url_video = str(request.args.get('url'))
    return "this is the url %s" % url_video

if __name__ == '__main__':
    app.run()