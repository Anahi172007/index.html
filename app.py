from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def inicio():
    nombre_sistema = "Sistema de Registro de Servicios"

    return render_template(
        "index.html",
        nombre_sistema=nombre_sistema
    )


@app.route("/servicios")
def servicios_page():

    servicios = [
        {
            "nombre": "Mantenimiento de computadoras",
            "precio": 25.00,
            "descripcion": "Limpieza y mantenimiento preventivo.",
            "disponible": True
        },
        {
            "nombre": "Instalación de software",
            "precio": 15.00,
            "descripcion": "Instalación y configuración de programas.",
            "disponible": True
        },
        {
            "nombre": "Diseño de página web",
            "precio": 50.00,
            "descripcion": "Creación de una página web básica.",
            "disponible": False
        },
        {
            "nombre": "Soporte técnico",
            "precio": 20.00,
            "descripcion": "Asistencia para problemas informáticos.",
            "disponible": True
        }
    ]

    return render_template(
        "servicios.html",
        servicios=servicios
    )


if __name__ == "__main__":
    app.run(debug=True)