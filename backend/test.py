from services.gpio_service import GpioService


def main():
    gpio = GpioService()

    print("Desactivando Carrier...")
    gpio.carrier_disable()

    print("Desactivando Auto Carrier...")
    gpio.auto_carrier_disable()

    print("Estado FAIL:", gpio.is_fail_active())


if __name__ == "__main__":
    main()