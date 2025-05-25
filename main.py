import time
import random
import psutil
import multiprocessing
import os
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


def log_sensor_data(instance_id):
    rooms = ['Lab A', 'Lab B', 'Conference Room', 'Lobby']
    loop_counter = 0

    while True:
        if loop_counter % 5 == 0:
            log_memory_usage()

        room = random.choice(rooms)
        temperature = read_temperature(room)
        co2 = read_co2_level(room)

        logger.info(f"[Instance {instance_id}] Sensor data | Room: {room} | Temperature: {temperature}C | CO2: {co2}ppm")

        if temperature > 24:
            logger.debug(f"[Instance {instance_id}] Temperature high in {room}: {temperature}C")

        if co2 > 1000:
            logger.warning(f"[Instance {instance_id}] CO2 levels elevated in {room}: {co2}ppm")

        sensor_data_cache.append({
            'room': room,
            'temperature': temperature,
            'co2': co2,
            'timestamp': time.time(),
            'trace': 'X' * 1000  # adds ~1kb of trace data
        })

        # Inject artificial error occasionally
        if random.random() < 0.05:
            logger.debug(f"[Instance {instance_id}] Cache size: {len(sensor_data_cache)}")
            try:
                raise ValueError("Random sensor malfunction detected.")
            except Exception as e:
                logger.error(f"[Instance {instance_id}] Sensor failure in {room}: {str(e)}", exc_info=True)

        loop_counter += 1
        time.sleep(0.5)


def worker(instance_id):
    # Optional: set CPU affinity (Linux only)
    try:
        cpu_core = instance_id % os.cpu_count()
        os.sched_setaffinity(0, {cpu_core})
        logger.info(f"[Instance {instance_id}] Bound to CPU core {cpu_core}")
    except AttributeError:
        # No affinity support on platform
        pass

    log_sensor_data(instance_id)

if __name__ == "__main__":
    num_instances = 4  # or how many you want
    processes = []

    for i in range(num_instances):
        p = multiprocessing.Process(target=worker, args=(i,), name=f"SensorInstance-{i}")
        p.start()
        processes.append(p)

    for p in processes:
        p.join()
