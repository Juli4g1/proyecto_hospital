# patient.py

import random
import time

class Patient:
    def __init__(self, patient_id):
        self.id = patient_id
        self.priority = random.randint(1, 3)  # 1 = más urgente
        self.status = "waiting"
        self.symptoms = self.generate_symptoms()
        self.diagnosis = None

    def generate_symptoms(self):
        symptoms_list = [
            "fiebre", "dolor de cabeza", "dificultad para respirar",
            "dolor abdominal", "mareo", "dolor en el pecho"
        ]
        return random.sample(symptoms_list, k=random.randint(1, 3))

    def run(self, resource_manager):
        print(f"\n👤 Procesando Paciente {self.id} (prioridad {self.priority})")
        print(f"🧾 Paciente {self.id} síntomas: {self.symptoms}")

        # Dinámica según prioridad
        if self.priority == 1:
            max_retries = 7
            wait_time = 2
        elif self.priority == 2:
            max_retries = 5
            wait_time = 5
        else:
            max_retries = 3
            wait_time = 7

        retry_count = 0
        success = False

        while retry_count < max_retries:
            success = resource_manager.assign_resources(self)
            if success:
                break
            retry_count += 1
            print(f"🔄 Paciente {self.id} reintenta ingreso ({retry_count}/{max_retries})")
            time.sleep(wait_time)

        if not success:
            self.status = "left"
            print(f"❌ Paciente {self.id} se retira tras {max_retries} intentos por falta de recursos")
            return

        self.status = "admitted"
        print(f"✅ Paciente {self.id} admitido al hospital")

    def __lt__(self, other):
        return self.priority < other.priority