import time
import random
import psutil
from logger import setup_logger


logger = setup_logger()

sensor_data_cache = []

def read_temperature(room: str) -> float:
    return round(18 + random.uniform(-3, 5), 2)

def read_co2_level(room: str) -> int:
    return random.randint(400, 1200)

def log_memory_usage():
    process = psutil.Process()
    mem_info = process.memory_info()
    logger.debug(f"Memory usage: {mem_info.rss / (1024 * 1024):.2f} MB | Cache size: {len(sensor_data_cache)}")


def log_sensor_data():
    rooms = ['Lab A', 'Lab B', 'Conference Room', 'Lobby']
    loop_counter = 0

    while True:
        if loop_counter % 5 == 0:
            log_memory_usage()

        room = random.choice(rooms)
        temperature = read_temperature(room)
        co2 = read_co2_level(room)

        logger.info(f"Sensor data | Room: {room} | Temperature: {temperature}C | CO2: {co2}ppm")

        if temperature > 24:
            logger.debug(f"Temperature high in {room}: {temperature}C")

        if co2 > 1000:
            logger.warning(f"CO2 levels elevated in {room}: {co2}ppm")

        sensor_data_cache.append({
            'room': room,
            'temperature': temperature,
            'co2': co2,
            'timestamp': time.time()
        })

        # Inject artificial error occasionally
        if random.random() < 0.05:
            logger.debug(f"Cache size: {len(sensor_data_cache)}")
            try:
                raise ValueError("Random sensor malfunction detected.")
            except Exception as e:
                logger.error(f"Sensor failure in {room}: {str(e)}", exc_info=True)

        loop_counter += 1
        time.sleep(2)

if __name__ == "__main__":
    try: 
        logger.info("Smart building logger started.")
        log_sensor_data()
    except:
        logger.debug("Program was exited unexpectedly..")
