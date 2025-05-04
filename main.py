# main.py

import threading
import queue
import asyncio
from diagnosis import diagnose
from patient import Patient
from resources import ResourceManager
from multiprocessing import Pool
from discharge import monitor_and_discharge
from utils.generate_report import generate_report

# Recursos globales (camas, doctores)
resource_manager = ResourceManager(total_beds=10, total_doctors=8)

# Cola de prioridad (1 es más urgente)
patient_queue = queue.PriorityQueue()

def patient_thread(patient_id):
    patient = Patient(patient_id)
    patient.run(resource_manager)
    asyncio.run(diagnose(patient))
    patient_queue.put(patient)

def simulate_patients(num_patients=10):
    threads = []
    patients = []

    for i in range(num_patients):
        patient = Patient(i + 1)
        t = threading.Thread(target=lambda: patient.run(resource_manager))
        threads.append(t)
        patients.append(patient)
        t.start()

    for t in threads:
        t.join()

    for patient in patients:
        print(f"\n👤 Procesando Paciente {patient.id}")
        print(f"🧾 Paciente {patient.id} síntomas: {patient.symptoms}")
        asyncio.run(diagnose(patient))
        patient_queue.put(patient)

    print("\n📋 Orden en la cola (por prioridad):")
    while not patient_queue.empty():
        patient = patient_queue.get()
        print(f"🔹 Paciente {patient.id} (prioridad {patient.priority})")

    follow_up_and_discharge(patients)
    generate_report(patients)


def follow_up_and_discharge(patients):
    admitted_patients = [p for p in patients if p.status == "admitted"]
    patient_data_list = [{'id': p.id} for p in admitted_patients]

    print(f"\n🏥 Iniciando seguimiento para {len(patient_data_list)} pacientes...\n")

    with Pool(processes=4) as pool:
        results = pool.map(monitor_and_discharge, patient_data_list)

    print("\n✅ Seguimiento y alta completados para:")
    for pid in results:
        print(f"📝 Paciente {pid}")


if __name__ == "__main__":
    simulate_patients(10)