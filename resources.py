# resources.py

import threading

class ResourceManager:
    def __init__(self, total_beds=10, total_doctors=8):
        self.total_beds = total_beds
        self.total_doctors = total_doctors
        self.available_beds = total_beds
        self.available_doctors = total_doctors
        self.lock = threading.Lock()

    def assign_resources(self, patient):
        with self.lock:
            print(f"🛏️ Camas disponibles: {self.available_beds}, Doctores disponibles: {self.available_doctors}")

            if self.available_beds > 0 and self.available_doctors > 0:
                self.available_beds -= 1
                self.available_doctors -= 1
                print(f"✅ Recursos asignados al paciente {patient.id}")
                return True
            else:
                print(f"❌ Recursos insuficientes para el paciente {patient.id}")
                return False

    def release_resources(self):
        with self.lock:
            self.available_beds += 1
            self.available_doctors += 1
            print("♻️ Recursos liberados")