import time

from hardware.ads1256.driver import ADS1256Controller


def main():

    adc = ADS1256Controller()

    try:
        print("Inicializando ADS1256...")

        adc.initialize()

        print("ADS1256 inicializado")
        print("------------------------")

        canales = [
            0x08,  # AIN0
            0x18,  # AIN1
            0x28,  # AIN2
            0x38,  # AIN3
            0x48,  # AIN4
            0x58,  # AIN5
            0x68   # AIN6
        ]

        while True:

            for i, canal in enumerate(canales):

                adc.channel(canal)

                valor = adc.read()

                print(
                    f"Canal {i}: {valor}"
                )

                time.sleep(0.2)

            print("------------------------")


    except KeyboardInterrupt:
        print("Test finalizado")

    finally:
        adc.close()


if __name__ == "__main__":
    main()