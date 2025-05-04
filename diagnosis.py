# diagnosis.py

import asyncio
import random
from models import mock_ai

async def diagnose(patient):
    print(f"💡 Diagnóstico IA para paciente {patient.id} en progreso...")
    
    # Preparar datos
    patient_data = {
        "id": patient.id,
        "symptoms": patient.symptoms
    }

    result = mock_ai.infer(patient_data)
    patient.diagnosis = result["diagnosis"]
    patient.priority = result["urgency"]

    print(f"💡 Diagnóstico IA para paciente {patient.id}: {patient.diagnosis} (urgencia {patient.priority})")