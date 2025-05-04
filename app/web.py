from flask import Flask, render_template, request, redirect, url_for
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from main import simulate_patients


app = Flask(__name__)

REPORT_DIR = os.path.join(os.path.dirname(__file__), "..", "reportes")

@app.route("/")
def dashboard():
    reportes = sorted(os.listdir(REPORT_DIR), reverse=True)
    return render_template("dashboard.html", reportes=reportes)

@app.route("/simular", methods=["POST"])
def simular():
    simulate_patients(10)
    return redirect(url_for("dashboard"))

@app.route("/reporte/<nombre>")
def ver_reporte(nombre):
    path = os.path.join(REPORT_DIR, nombre)
    if not os.path.exists(path):
        return "Reporte no encontrado", 404
    with open(path, encoding="utf-8") as f:
        contenido = f.read()
    return f"<pre>{contenido}</pre>"

if __name__ == "__main__":
    app.run(debug=True)