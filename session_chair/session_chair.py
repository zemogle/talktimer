
import time
from blink1.blink1 import Blink1
import click
import random
import atexit

b1 = Blink1()

def tear_down():
    b1.fade_to_rgb(1000, 0, 0, 0)
    print("Talk Timer stopped")
    b1.close()
    return

atexit.register(tear_down)

@click.command()
@click.option('--total', '-t', help='Total length of talk.', type=int)
@click.option('--warning', '-w', help='Time before the end you will give a warning', type=int)
@click.option('--seconds', '-s', help='Give the time in seconds', default=False, is_flag=True)
def blink_timer(total, warning, seconds):
    subtotal = total - warning
    if not seconds:
        seconds = 60
    else:
        seconds = 1
    b1.fade_to_rgb(1000, 0, 255, 0)
    time.sleep(subtotal*seconds)
    b1.fade_to_rgb(1000, 255,163,0)
    time.sleep(warning*seconds)
    b1.fade_to_rgb(1000, 255, 0, 0)
    time.sleep(20)

    blink_go_crazy()
    b1.close()
    return

def blink_go_crazy():
    for i in range(0,10000):
        red = random.randint(0,255)
        green = random.randint(0,255)
        blue = random.randint(0,255)
        led_number = random.randint(0,2)
        b1.fade_to_rgb(1, red, green, blue, led_number)
        time.sleep(0.01)
    return
