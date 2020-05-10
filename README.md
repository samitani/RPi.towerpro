# RPi.towerpro
library to control TowerPro servo motors, by software PWM.

# example
```
import towerpro
import time

INTERVAL = 1

sg90 = towerpro.TowerProServo(pin=14)

for i in range(10):
    sg90.rotate(-90 + i * 20)
    time.sleep(INTERVAL)
```
