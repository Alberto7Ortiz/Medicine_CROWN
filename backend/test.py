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
            0x10,  # AIN1
            0x20,  # AIN2
            0x30,  # AIN3
            0x40,  # AIN4
            0x50,  # AIN5
            0x60,  # AIN6
            0x70   # AIN7
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