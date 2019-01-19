from flask import Flask, render_template, jsonify, request
from flask_bootstrap import Bootstrap
import base64
from hashlib import md5
from DetectingFace import *
"""

"""
app = Flask(__name__)
bootstrap = Bootstrap(app)


@app.route("/")
def index():
    return render_template("index.html")

@app.route('/detect-face', methods=['POST'])
def detect_face():
    # TODO:
    #kill_me = {"Name":"Cruz Hacks" , "Project":"ALzheimers"}
    
    img_content = request.data
    decoded_img = base64.b64decode(img_content)
    #API CALL RIGHT HERE
    #print(decoded_img)
    # Temporarily save image as file
    img_path = "uploads/" + md5(img_content.decode().encode('utf-8')).hexdigest() + ".png"
    with open(img_path, "wb") as fh:
        fh.write(decoded_img)
    result = return_message_from_face(img_path)
    result['msg'] = "You met Tejas at Robotics camp."
    return jsonify(result) # will have to returned json dat from API call

if __name__=='__main__':
    app.run(debug=True)
