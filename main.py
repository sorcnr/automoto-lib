from machine import Pin,Timer

led = Pin(2,Pin.OUT)

tim = Timer(0)
def toggle():
    led.value(not led.value())

    return print("Led value has changed to {}".format(led.value()))

#tim.init(period=1000,mode=Timer.PERIODIC,callback=lambda t:toggle())