import flask
import sys
from PIL import Image
import base64
import json
from model import detector, run_detector
import cv2
# from model import run_detector, detector
app = flask.Flask(__name__)


@app.route("/", methods=["POST"])
def detect():
    #if image was submitted
    obj = flask.request.get_json()
    img = obj['image']
    imgdata = base64.b64decode(img)
    result = run_detector(detector, imgdata)
    result_img = base64.b64encode(cv2.imencode('.jpg', result[0])[1]).decode()
    result_time = result[1]
    return flask.jsonify(
        {'image': result_img,
        'time': result_time}
    )

    
    
    

# start the flask app, allow remote connections
# app.run(host='0.0.0.0')
app.run(debug = True)

