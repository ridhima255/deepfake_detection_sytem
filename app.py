from flask import Flask, render_template, request
import os
from detect import predict_image

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():

    result = ""

    if request.method == 'POST':
        file = request.files['file']
        filepath = os.path.join("static", file.filename)
        file.save(filepath)

        result = predict_image(filepath)

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)