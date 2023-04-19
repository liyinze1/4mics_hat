from pixels import pixels
import time

while True:

    try:
        pixels.wakeup()
        time.sleep(3)
        pixels.think()
        time.sleep(3)
        pixels.speak()
        time.sleep(3)
    except KeyboardInterrupt:
        break

pixels.off()
time.sleep(1)