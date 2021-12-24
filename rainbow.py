import time
import board
import adafruit_dotstar
import atexit
import signal

kill_now = False
DOTSTAR_DATA = board.D5
DOTSTAR_CLOCK = board.D6

dots = adafruit_dotstar.DotStar(DOTSTAR_CLOCK, DOTSTAR_DATA, 3, brightness=0.5)

def exit_handler():
    kill_now = True
    # turn off the pixel dots
    for i in range(3):
        dots[i] = (0,0,0)
    dots.show()

atexit.register(exit_handler)
signal.signal(signal.SIGINT, exit_handler)
signal.signal(signal.SIGTERM, exit_handler)

def wheel(pos):
    # Input a value 0 to 255 to get a color value.
    # The colours are a transition r - g - b - back to r.
    if pos < 0 or pos > 255:
        return (0, 0, 0)
    if pos < 85:
        return (255 - pos * 3, pos * 3, 0)
    if pos < 170:
        pos -= 85
        return (0, 255 - pos * 3, pos * 3)
    pos -= 170
    return (pos * 3, 0, 255 - pos * 3)

while not kill_now:
    for j in range(255):
        for i in range(3):
            rc_index = (i * 256 // 3) + j * 5
            dots[i] = wheel(rc_index & 255)
        dots.show()
        time.sleep(0.01)
