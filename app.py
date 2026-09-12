from flask import Flask, render_template

app = Flask(__name__)

hombres = [
    {"nombre": "NIKE DUNK SB", "precio": "$100.000", "imagen": "/static/imagen1.png"},
    {"nombre": "AIR JORDAN RETRO 1 LOW", "precio": "$105.000", "imagen": "/static/imagen2.png"},
    {"nombre": "ADIDAS NASTASE", "precio": "$100.000", "imagen": "/static/imagen3.png"},
    {"nombre": "AIR JORDAN RETRO 1", "precio": "$120.000", "imagen": "/static/imagen4.png"},
    {"nombre": "AIR JORDAN 4", "precio": "$100.000", "imagen": "/static/imagen5.png"},
    {"nombre": "AIR JORDAN RETRO 3", "precio": "$120.000", "imagen": "/static/imagen6.png"},
    {"nombre": "AIR JORDAN RETRO 11", "precio": "$140.000", "imagen": "/static/imagen7.png"},
    {"nombre": "AIR JORDAN RETRO 3", "precio": "$120.000", "imagen": "/static/imagen71.png"},
    {"nombre": "AIR JORDAN RETRO 1 LOW", "precio": "$120.000", "imagen": "/static/imagen72.png"},
    {"nombre": "LECOQ SPORTIF", "precio": "$110.000", "imagen": "/static/imagen73.png"},
    {"nombre": "PUMA SUEDE X BMW", "precio": "$120.000", "imagen": "/static/imagen74.png"},
    {"nombre": "LECOQ SPORTIF", "precio": "$100.000", "imagen": "/static/imagen75.png"},
    {"nombre": "VANS HYLANE", "precio": "$120.000", "imagen": "/static/imagen76.png"},
    {"nombre": "OFF WHITE", "precio": "$120.000", "imagen": "/static/imagen77.png"},
    {"nombre": "ADIDAS SUPERSTAR", "precio": "$120.000", "imagen": "/static/imagen78.png"},
    {"nombre": "NIKE CORTEZ", "precio": "$110.000", "imagen": "/static/imagen79.png"},
        
]

damas = [
    {"nombre": "NIKE SKATE", "precio": "$100.000", "imagen": "/static/imagen8.png"},
    {"nombre": "ADIDAS SUPER STAR", "precio": "$110.000", "imagen": "/static/imagen9.png"},
    {"nombre": "AIR JORDAN RETRO 1 LOW", "precio": "$105.000", "imagen": "/static/imagen10.png"},
    {"nombre": "ADIDAS SPEZIAL", "precio": "$120.000", "imagen": "/static/imagen12.png"},
    {"nombre": "ADIDAS SAMBA", "precio": "$120.000", "imagen": "/static/imagen13.png"},
]

@app.route("/")
def inicio():
    return render_template("index.html", hombres=hombres, damas=damas)

if __name__ == "__main__":
    app.run(debug=True)