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
    {"nombre": "ADIDAS GLOW", "precio": "$120.000", "imagen": "/static/imagen80.png"},
    {"nombre": "ADIDAS GLOW", "precio": "$120.000", "imagen": "/static/imagen81.png"},
    {"nombre": "ADIDAS ADISTAR", "precio": "$125.000", "imagen": "/static/imagen82.png"},
    {"nombre": "NIKE VOMERO PLUS", "precio": "$120.000", "imagen": "/static/imagen83.png"},
    
    
    
    
    
    
    
]

damas = [
    {"nombre": "NIKE SKATE", "precio": "$100.000", "imagen": "/static/imagen8.png"},
    {"nombre": "ADIDAS SUPER STAR", "precio": "$110.000", "imagen": "/static/imagen9.png"},
    {"nombre": "AIR JORDAN RETRO 1 LOW", "precio": "$105.000", "imagen": "/static/imagen10.png"},
    {"nombre": "SANDALIA DIOR", "precio": "$120.000", "imagen": "/static/imagen11.png"},
    {"nombre": "ADIDAS SPEZIAL", "precio": "$120.000", "imagen": "/static/imagen12.png"},
    {"nombre": "ADIDAS SAMBA", "precio": "$120.000", "imagen": "/static/imagen13.png"},
    {"nombre": "ADIDAS PUREBOOST", "precio": "$120.000", "imagen": "/static/imagen14.png"},
    {"nombre": "NEW BALANCE 574", "precio": "$120.000", "imagen": "/static/imagen15.png"},
    {"nombre": "NIKE DUNK SB LOW", "precio": "$125.000", "imagen": "/static/imagen16.png"},
    {"nombre": "AIR JORDAN RETRO 1", "precio": "$125.000", "imagen": "/static/imagen17.png"},
    {"nombre": "NIKE DUNK SB", "precio": "$120.000", "imagen": "/static/imagen18.png"},
    {"nombre": "PUMA PASK", "precio": "$120.000", "imagen": "/static/imagen19.png"},
    {"nombre": "LECOQ SPORTIF", "precio": "$110.000", "imagen": "/static/imagen20.png"},
    {"nombre": "AIR JORDANRETRO 3", "precio": "$120.000", "imagen": "/static/imagen21.png"},
    {"nombre": "ADIDAS SAMBA", "precio": "$120.000", "imagen": "/static/imagen22.png"},
    {"nombre": "NEW BALANCE 530", "precio": "$120.000", "imagen": "/static/imagen23.png"},
    {"nombre": "ADIDAS NIZZA", "precio": "$100.000", "imagen": "/static/imagen24.png"},
    {"nombre": "ADIDAS NIZZA", "precio": "$100.000", "imagen": "/static/imagen25.png"},
    {"nombre": "ADIDAS SUPERSTAR", "precio": "$100.000", "imagen": "/static/imagen26.png"},
    {"nombre": "ADIDAS SUPERSTAR", "precio": "$100.000", "imagen": "/static/imagen27.png"},
    {"nombre": "NIKE VK", "precio": "$120.000", "imagen": "/static/imagen28.png"},
    {"nombre": "ADIDAS GLOW", "precio": "$120.000", "imagen": "/static/imagen29.png"},
    {"nombre": "ADIDAS GLOW", "precio": "$120.000", "imagen": "/static/imagen30.png"},
    {"nombre": "NEW BALANCE 530 EMCAP", "precio": "$110.000", "imagen": "/static/imagen31.png"},
    {"nombre": "ADIDAS MAGMA", "precio": "$120.000", "imagen": "/static/imagen32.png"},
    {"nombre": "ADIDAS MAGMA", "precio": "$120.000", "imagen": "/static/imagen33.png"},
    {"nombre": "ADIDAS MAGMA", "precio": "$120.000", "imagen": "/static/imagen34.png"},
    {"nombre": "NIKE VOMERO PLUS", "precio": "$120.000", "imagen": "/static/imagen35.png"},
    {"nombre": "NIKE VOMERO PLUS", "precio": "$120.000", "imagen": "/static/imagen36.png"},
    {"nombre": "NIKE COMFORT RIDE", "precio": "$120.000", "imagen": "/static/imagen37.png"},
    
    
    
]

@app.route("/")
def inicio():
    return render_template("index.html", hombres=hombres, damas=damas)


@app.route("/hombres")
def pagina_hombres():
    return render_template("hombres.html", hombres=hombres)


@app.route("/damas")
def pagina_damas():
    return render_template("damas.html", damas=damas)


@app.route("/contacto")
def pagina_contacto():
    return render_template("contacto.html")


if __name__ == "__main__":
    app.run(debug=True)