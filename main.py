import spidev
import time
import RPi.GPIO as GPIO

def toVolt(read, v = 3.3):
    return read * v / 1023

def toRead(volt):
    return volt * 1023 / 3.3


spi = spidev.SpiDev()

spi.open(0, 0)
spi.max_speed_hz = 100000

GPIO.setmode(GPIO.BCM)
GPIO.setup(14, GPIO.OUT)

def analog_read(channel):
    ret = spi.xfer2([1, (8 + channel) << 4, 0])
    adc_out = ((ret[1] & 3) << 8) + ret[2]
    return adc_out

try:
    while 1:
        ldr_value = analog_read(0)
        print("LDR Value: %s        V: %s" % (ldr_value, toVolt(ldr_value)))
        if ldr_value < 512:
            GPIO.output(14, 1)
        else:
            GPIO.output(14, 0)
        time.sleep(0.5)
finally:
    spi.close()
