from cnfont import chinese,pixel,image,anime1,anime2,anime3,flx,anime0
import max7219
from machine import Pin, SPI,freq
import time
from sys import platform
import uasyncio as asyncio
ESP32 = platform == 'esp32' or platform == 'esp32_LoBo'
from aremote import *

spi = SPI(1, baudrate=4000000, polarity=1, phase=0, sck=Pin(4), mosi=Pin(2))
ss = Pin(5, Pin.OUT)
display = max7219.Matrix8x8(spi, ss, 16)


l1="大佬让我过去吧"
l2="祝您身体健康"
l3="财源广进"









# flx(l1,display)
# flx(l2)
# flx(l3)
# time.sleep(2)


anime0("爱一直在",display)
# anime1("下次一定",display)
# anime2("一键三连",display)
# anime3("拒绝白嫖",display)

image("b.json",display)

errors = {BADSTART : 'Invalid start pulse', BADBLOCK : 'Error: bad block',
          BADREP : 'Error: repeat', OVERRUN : 'Error: overrun',
          BADDATA : 'Error: invalid data', BADADDR : 'Error: invalid address'}

def cb(data, addr):
    if data >0:
        print(data)
        if data==8:
            flx(l1,display,'l')
            flx(l2,display,'l')
            flx(l3,display,'l')
        elif data==90:
            flx(l1,display,'r')
            flx(l2,display,'r')
            flx(l3,display,'r')
        elif data==28:
            anime1("谢谢大佬",display)
            anime3("大佬最美",display)
        elif data==69:
            image("b.json",display)
        elif data==70:
            image("d.json",display)
        elif data==68:
            anime2("一键三连",display)
        elif data==64:
            anime2("下次一定",display)
        elif data==67:
            anime2("拒绝白嫖",display)
        elif data==71:
            anime0("一键三连",display)
        elif data==7:
            anime3("日你仙人",display)
        else:
            display.fill(0)
            display.show()
def test():
    print('Test for IR receiver. Assumes NEC protocol.')
    print('ctrl-c to stop.')
    p = Pin(23, Pin.IN)
    ir = NEC_IR(p, cb, True)  # Assume r/c uses extended addressing
    loop = asyncio.get_event_loop()
    try:
        loop.run_forever()
    except KeyboardInterrupt:
        print('Interrupted')
    finally:
        asyncio.new_event_loop()  # Still need ctrl-d because of interrupt vector

test()