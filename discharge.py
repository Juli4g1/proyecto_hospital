# discharge.py

import time
import random

def monitor_and_discharge(patient_data):
    patient_id = patient_data['id']
    duration = random.uniform(2.0, 4.0)

    print(f"🔬 Seguimiento en curso para Paciente {patient_id}...")
    time.sleep(duration)

    print(f"📤 Alta emitida para Paciente {patient_id} tras {duration:.2f} segundos")
    return patient_id