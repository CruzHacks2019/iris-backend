from flask import Flask, render_template, jsonify, request
from flask_bootstrap import Bootstrap
import base64
from hashlib import md5
from APIClient import *
"""

"""
app = Flask(__name__)
bootstrap = Bootstrap(app)
client = APIClient("people_three")

@app.route("/")
def index():
    return render_template("index.html")

@app.route('/detect-face', methods=['POST'])
def detect_face():
    img_content = request.data
    decoded_img = base64.b64decode(img_content)
    img_path = "uploads/" + md5(img_content.decode().encode('utf-8')).hexdigest() + ".png"
    with open(img_path, "wb") as fh:
        fh.write(decoded_img)

    result = client.return_message_from_face(img_path)
    result['msg'] = "You met " + result["name"] + " he is your " + result["userData"] + "."
    return jsonify(result)

if __name__=='__main__':
    app.run(debug=True)
