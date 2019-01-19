from flask import Flask, render_template, jsonify
from flask_bootstrap import Bootstrap
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
    kill_me = {"Name":"Cruz Hacks" , "Project":"ALzheimers"}
    return jsonify(kill_me)

if __name__=='__main__':
    app.run(debug=True)
