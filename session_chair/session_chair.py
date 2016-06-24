
import time
from blink1.blink1 import blink1
import click
import random

def init():
    if ( blink1.dev == None ):
        print("You didn't plug in the blink(1), dummy")
    else:
        print("blink(1) found")

@click.command()
@click.option('--total', '-t', default=15, help='Total length of talk.')
@click.option('--warning', '-w', default=1, help='Time before the end you will give a warning')
@click.option('--seconds', '-s', help='Give the time in seconds', default=False, is_flag=True)
def blink_timer(total, warning, seconds):
    #init()
    subtotal = total - warning
    if not seconds:
        seconds = 60
    else:
        seconds = 1
    with blink1() as b1:
        b1.fade_to_rgb(1000, 0, 255, 0)
        time.sleep(subtotal*seconds)
        b1.fade_to_rgb(1000, 0, 0, 255)
        time.sleep(warning*seconds)
        b1.fade_to_rgb(1000, 255, 0, 0)
        time.sleep(20)

        blink_go_crazy(b1)
    b1.close()
    return

def blink_go_crazy(b1):
    for i in range(0,10000):
        red = random.randint(0,255)
        green = random.randint(0,255)
        blue = random.randint(0,255)
        led_number = random.randint(0,2)
        b1.fade_to_rgb(1, red, green, blue, led_number)
        time.sleep(0.01)
    return
