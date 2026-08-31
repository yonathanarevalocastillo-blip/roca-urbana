from flask import Flask, render_template

app = Flask(__name__)

hombres = [
    {"nombre": "Urban Black", "precio": "$99.000", "imagen": "/static/13.png"},
    {"nombre": "White Street", "precio": "$105.000", "imagen": "/static/4.png"},
    {"nombre": "Classic Urban", "precio": "$110.000", "imagen": "/static/5.png"},
    {"nombre": "Classic 1", "precio": "$150.000", "imagen": "/static/6.png"},
    {"nombre": "Classic 2", "precio": "$180.000", "imagen": "/static/7.png"},
    {"nombre": "Classic 3", "precio": "$200.000", "imagen": "/static/8.png"},
]

damas = [
    {"nombre": "Classic 4", "precio": "$200.000", "imagen": "/static/9.png"},
    {"nombre": "Classic 5", "precio": "$200.000", "imagen": "/static/10.png"},
    {"nombre": "Classic 6", "precio": "$200.000", "imagen": "/static/12.png"},
]

@app.route("/")
def inicio():
    return render_template("index.html", hombres=hombres, damas=damas)

if __name__ == "__main__":
    app.run(debug=True)