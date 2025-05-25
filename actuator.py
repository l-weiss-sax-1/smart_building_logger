import time
import random

class ActuatorController:
    def __init__(self):
        self.devices = {
            'AC': False,
            'VentilationFan': False,
            'Alarm': False
        }

    def activate_device(self, device_name):
        if device_name in self.devices:
            self.devices[device_name] = True
            time.sleep(0.2 * random.random())  # simulate delay
        else:
            raise ValueError(f"Unknown device: {device_name}")

    def deactivate_all(self):
        for device in self.devices:
            self.devices[device] = False

    def get_status(self):
        return self.devices.copy()
