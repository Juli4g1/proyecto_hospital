# models/mock_ai.py

import asyncio
import random

# Reglas simples para simular un "modelo" de diagnóstico
def infer(patient_data):
    symptoms = patient_data.get("symptoms", [])

    # Diagnósticos posibles y lógica simple basada en síntomas
    diagnosis = "Revisión general"
    urgency = 3  # urgencia baja por defecto

    if "dificultad para respirar" in symptoms and "dolor en el pecho" in symptoms:
        diagnosis = "Posible ataque cardíaco o problema respiratorio grave"
        urgency = 1
    elif "fiebre" in symptoms and "dolor de cabeza" in symptoms:
        diagnosis = "Posible infección viral"
        urgency = 2
    elif "dolor abdominal" in symptoms and "mareo" in symptoms:
        diagnosis = "Deshidratación o problema digestivo"
        urgency = 2
    elif "dolor en el pecho" in symptoms:
        diagnosis = "Evaluación cardíaca necesaria"
        urgency = 1
    elif "mareo" in symptoms:
        diagnosis = "Chequeo neurológico sugerido"
        urgency = 3
    elif "dolor abdominal" in symptoms:
        diagnosis = "Sospecha de gastritis o apendicitis"
        urgency = 2
    elif "fiebre" in symptoms:
        diagnosis = "Síntomas virales leves"
        urgency = 3
    else:
        diagnosis = "Observación general"
        urgency = random.choice([2, 3])

    return {
        "diagnosis": diagnosis,
        "urgency": urgency
    }