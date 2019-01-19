from flask import Flask, render_template, jsonify
from flask_bootstrap import Bootstrap
import base64
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
    
    img_content = request.body
    decoded_img = base64.b64decode(img_content)
    #API CALL RIGHT HERE
    #print(decoded_img)
    # Temporarily save image as file
    with open("imageToSave.png", "wb") as fh:
        fh.write(decoded_img)
    return jsonify(decoded_img) # will have to returned json dat from API call

if __name__=='__main__':
    app.run(debug=True)
