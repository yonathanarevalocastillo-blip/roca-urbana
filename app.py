from flask import Flask, render_template

app = Flask(__name__)

hombres = [
    
    {"nombre": "White Street", "precio": "$105.000", "imagen": "/static/imagen1.png"},
    {"nombre": "Classic Urban", "precio": "$110.000", "imagen": "/static/imagen2.png"},
    {"nombre": "Classic 1", "precio": "$150.000", "imagen": "/static/imagen3.png"},
    {"nombre": "Classic 2", "precio": "$180.000", "imagen": "/static/imagen4.png"},
    {"nombre": "Classic 3", "precio": "$200.000", "imagen": "/static/imagen5.png"},
    {"nombre": "Classic 3", "precio": "$200.000", "imagen": "/static/imagen6.png"},
    {"nombre": "Classic 3", "precio": "$200.000", "imagen": "/static/imagen7.png"},
    
]

damas = [
    {"nombre": "Classic 4", "precio": "$200.000", "imagen": "/static/imagen8.png"},
    {"nombre": "Classic 4", "precio": "$200.000", "imagen": "/static/imagen9.png"},
    {"nombre": "Classic 5", "precio": "$200.000", "imagen": "/static/imagen10.png"},
    {"nombre": "Classic 6", "precio": "$200.000", "imagen": "/static/imagen12.png"},
    {"nombre": "Classic 6", "precio": "$200.000", "imagen": "/static/imagen13.png"}, 
     
]

@app.route("/")
def inicio():
    return render_template("index.html", hombres=hombres, damas=damas)

if __name__ == "__main__":
    app.run(debug=True)