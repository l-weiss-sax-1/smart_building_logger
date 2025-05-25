class AnomalyDetector:
    def __init__(self):
        self.last_temperatures = {}

    def detect(self, room, temperature, co2):
        anomalies = []

        if temperature > 26:
            anomalies.append("High temperature")

        if co2 > 1100:
            anomalies.append("Very high CO2")

        last_temp = self.last_temperatures.get(room)
        if last_temp and abs(temperature - last_temp) > 5:
            anomalies.append("Sudden temperature swing")

        self.last_temperatures[room] = temperature

        return anomalies
