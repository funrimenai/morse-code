from flask import Flask, request, render_template
import pandas as pd

app = Flask(__name__)

df = pd.read_csv("static/assets/code.csv")
morse_code_map = dict(zip(df.letter.str.strip(), df.morse.str.strip()))


def convert_to_morse(text):
    morse_code = ""
    for letter in text.upper():
        if letter in morse_code_map:
            morse_code += morse_code_map[letter] + ' '
        else:
            morse_code += letter
    return morse_code.strip()


@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        normal_text = request.form["normalText"]
        morse_code = convert_to_morse(normal_text)
        return render_template("index.html", normal_text=normal_text, morse_code=morse_code)
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True, port=5002)
