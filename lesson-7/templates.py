"""
templates usando jinja2

OBS.: Visualizar conteúdo página html
view-source:https://www.google.com.br/
"""

from flask import Flask, render_template

app = Flask("__name__", template_folder="template")

@app.route("/")
def index():
    x=10
    y=5
    return render_template("index.html", x=x, z=y)

if __name__ == "__main__":
    app.run(debug=True)