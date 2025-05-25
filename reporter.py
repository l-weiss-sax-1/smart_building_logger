import random
import time

class ExternalReporter:
    def __init__(self, failure_rate=0.2):
        self.failure_rate = failure_rate

    def report(self, payload):
        start = time.time()
        time.sleep(random.uniform(0.05, 0.3))  # simulate network delay

        if random.random() < self.failure_rate:
            raise ConnectionError("Failed to connect to external service.")
        return {"status": "ok", "received": payload}
