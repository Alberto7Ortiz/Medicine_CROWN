import RPi.GPIO as GPIO
import spidev
import time

from hardware.gpio.pins import Pins
from hardware.ads1256.registers import Commands

class ADS1256Controller:

#-----------------------
# __init__
#-----------------------
    def __init__(self):
        #Hardware
        self.spi=spidev.SpiDev()
        
#-----------------------
# initialize
#-----------------------
    def initialize(self):
        GPIO.setwarnings(False)
        GPIO.cleanup()
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(Pins.DRDY, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        
        self.spi.open(0,0)		    	# bus 0, CE0
        self.spi.max_speed_hz = 1000000	# 1 MHz (seguro)
        self.spi.mode = 1 		    	# ADS1256 usa SPI mode1
        self.spi.no_cs = True

        GPIO.setup(Pins.CS,GPIO.OUT)
        GPIO.output(Pins.CS,1)
        
        self.reset()
        self.first_conf()
        self.wait_drdy()

#-----------------------------------
# Wait DRDY 
#-----------------------------------
    def wait_drdy(self):
        while GPIO.input(Pins.DRDY):
            pass

#-----------------------------------
# Basic Commands 
#-----------------------------------
    #Command Reset
    def reset(self):
        GPIO.output(Pins.CS,0)
        self.spi.xfer([Commands.CMD_RESET])
        GPIO.output(Pins.CS,1)
        time.sleep(0.001)   #en realidad hay que esperar 33us
        self.wait_drdy()
        self.read()
    
    #Comand Read
    def read(self):
        self.wait_drdy()
        GPIO.output(Pins.CS,0)
        raw=self.spi.xfer2([Commands.CMD_RDATA])
        time.sleep(0.00000651)                  #6.51us porque la frecuencia es 7.68 MHz
        raw=self.spi.xfer([0x00,0x00,0x00])
        GPIO.output(Pins.CS,1)
        value = (raw[0] << 16) | (raw[1] << 8) | raw [2]
        # convertir signo (complemento a 2)
        if value & 0x800000:
            value -= 1 << 24
        return value
    
    #Close de SPI
    def close(self):
        self.spi.close()


#-----------------------------------
# Functions 
#-----------------------------------

    # This is the firs configuration after reset
    def first_conf(self):
        GPIO.output(Pins.CS,0)
        self.spi.xfer2([Commands.CMD_SYNC,Commands.CMD_WAKEUP,Commands.CMD_WREG | Commands.REG_STATUS, 0x03, Commands.INI_STATUS, Commands.INI_MUX, Commands.INI_ADCON, Commands.INI_DRATE])    
        GPIO.output(Pins.CS,1)


    #Select the chanel, only works with these valius 0x10,0x20,0x30,0x40,0x50,0x60,0x70
    def channel(self, ch):
        self.wait_drdy()

        GPIO.output(Pins.CS,0)
        self.spi.xfer2([Commands.CMD_WREG | Commands.REG_MUX ,0x00 , ch])
        self.spi.xfer2([Commands.CMD_SYNC])
        self.spi.xfer2([Commands.CMD_WAKEUP])
        self.spi.xfer2([Commands.CMD_RDATA])
        time.sleep(0.00000651)                  #6.51us porque la frecuencia es 7.68 MHz
        self.spi.xfer([0x00,0x00,0x00])
        GPIO.output(Pins.CS,1)

        self.wait_drdy()
        GPIO.output(Pins.CS,0)
        self.spi.xfer2([Commands.CMD_RDATA])
        time.sleep(0.00000651)                  #6.51us porque la frecuencia es 7.68 MHz
        self.spi.xfer([0x00,0x00,0x00])
        GPIO.output(Pins.CS,1)  


