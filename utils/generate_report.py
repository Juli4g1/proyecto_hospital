# utils/generate_report.py

import os
from datetime import datetime

def generate_report(patients, folder="reportes"):
    if not os.path.exists(folder):
        os.makedirs(folder)

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"{folder}/reporte_hospital_{timestamp}.txt"

    with open(filename, "w", encoding="utf-8") as f:
        f.write(f"📄 Reporte generado: {timestamp}\n")
        f.write("=" * 50 + "\n")

        for patient in patients:
            f.write(f"👤 Paciente {patient.id}\n")
            f.write(f"🩺 Síntomas: {', '.join(patient.symptoms)}\n")
            f.write(f"📋 Diagnóstico: {patient.diagnosis}\n")
            f.write(f"⚠️ Nivel de urgencia: {patient.priority}\n")
            f.write(f"🏥 Estado final: {patient.status}\n")
            f.write("-" * 50 + "\n")

    print(f"\n✅ Reporte generado en: {filename}")