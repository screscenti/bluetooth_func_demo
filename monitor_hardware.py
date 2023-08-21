import psutil
from pysmart.smart import Smart

def get_cpu_temperature():
    temperatures = psutil.sensors_temperatures()
    if "coretemp" in temperatures:
        return temperatures["coretemp"][0].current
    else:
        # Adjust based on your hardware
        # Not all hardware is supported
        return None

def get_memory_usage():
    memory_info = psutil.virtual_memory()
    return memory_info.percent

def get_disk_usage():
    return psutil.disk_usage('/').percent

def get_hdd_temperature():
    s = Smart()
    hdd_temp = None
    for disk in s.disks:
        if disk is not None and disk.temperature:
            hdd_temp = disk.temperature
            break
    return hdd_temp

if __name__ == "__main__":
    print(f"CPU Temperature: {get_cpu_temperature()}°C")
    print(f"Memory Usage: {get_memory_usage()}%")
    print(f"Disk Usage: {get_disk_usage()}%")
    print(f"HDD/SSD Temperature: {get_hdd_temperature()}°C")
