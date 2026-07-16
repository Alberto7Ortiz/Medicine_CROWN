from services.system_service import SystemService


service = SystemService()

status = service.get_system_status()

print(status)