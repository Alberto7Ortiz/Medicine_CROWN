import os
import shutil


class SystemMonitor:

    def __init__(self):
        pass

    def get_cpu_temperature(self):
        """
        Obtiene la temperatura del CPU de la Raspberry Pi.
        """
        try:
            with open("/sys/class/thermal/thermal_zone0/temp", "r") as file:
                temperature = int(file.read()) / 1000
                return round(temperature, 2)

        except Exception:
            return None


    def get_cpu_usage(self):
        """
        Obtiene el porcentaje de uso del CPU.
        """
        try:
            load = os.getloadavg()[0]
            cpu_count = os.cpu_count()

            usage = (load / cpu_count) * 100

            return round(usage, 2)

        except Exception:
            return None


    def get_memory_usage(self):
        """
        Obtiene el porcentaje de memoria RAM utilizada.
        """
        try:
            with open("/proc/meminfo", "r") as file:
                data = file.readlines()

            total = None
            available = None

            for line in data:
                if line.startswith("MemTotal"):
                    total = int(line.split()[1])

                if line.startswith("MemAvailable"):
                    available = int(line.split()[1])

            if total and available:
                used = total - available
                percentage = (used / total) * 100

                return round(percentage, 2)

            return None

        except Exception:
            return None


    def get_storage_usage(self):
        """
        Obtiene el porcentaje de almacenamiento utilizado.
        """
        try:
            total, used, free = shutil.disk_usage("/")

            percentage = (used / total) * 100

            return round(percentage, 2)

        except Exception:
            return None