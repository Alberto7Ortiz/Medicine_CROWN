from hardware.raspberry.system_monitor import SystemMonitor


class SystemService:

    def __init__(self):
        self.monitor = SystemMonitor()


    def get_system_status(self):
        """
        Devuelve el estado general del sistema Raspberry.
        """

        return {
            "temperature": self.monitor.get_cpu_temperature(),
            "cpu_usage": self.monitor.get_cpu_usage(),
            "ram_usage": self.monitor.get_memory_usage(),
            "storage_usage": self.monitor.get_storage_usage()
        }