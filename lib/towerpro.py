import RPi.GPIO as GPIO

class TowerProServo():

    def __init__(self, pin):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(pin, GPIO.OUT)
        self.servo = GPIO.PWM(pin, 50)
        self.servo.start(0.0)

    def rotate(self, angle):
        if (angle < -90 or angle > 90):
            return False

        self.servo.ChangeDutyCycle(self.getduty(angle))

    def getduty(self, angle):
        cycle = 0.5 + (1.9) * ((angle + 90.0) / 180.0)
        duty = round(cycle / 20.0 * 100.0, 1)
    
        print(duty)

    	return duty
     
    def __destory__(self):
        GPIO.cleanup()
