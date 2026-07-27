from database.repository import Repository

from services.acquisition import AcquisitionService



# ==================================
# Fake ADS1256
# ==================================

class FakeADC:


    def initialize(self):

        print("ADC initialized")



    def channel(self, channel):

        print(
            "Reading channel:",
            hex(channel)
        )



    def read(self):

        # Valor simulado ADC

        return 1000000



    def close(self):

        print("ADC closed")



# ==================================
# Fake GPIO
# ==================================

class FakeGPIO:


    def get_carrier_status(self):

        return True



    def get_auto_carrier_status(self):

        return False



    def is_fail_active(self):

        return False



# ==================================
# TEST
# ==================================

def main():


    print(
        "\nStarting acquisition test\n"
    )


    repository = Repository()


    adc = FakeADC()

    gpio = FakeGPIO()



    service = AcquisitionService(

        adc_controller=adc,

        gpio_service=gpio,

        repository=repository

    )



    print(
        "Starting service..."
    )


    service.start()



    # Esperar algunas lecturas

    import time

    time.sleep(1)



    measurement = (
        service.get_last()
    )


    print(
        "\nMeasurement:"
    )


    print(measurement)



    assert measurement is not None



    assert "analog" in measurement

    assert "digital" in measurement



    print(
        "\nAcquisition test OK"
    )



    service.stop()

    repository.close()



if __name__ == "__main__":

    main()