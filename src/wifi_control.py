# adapted from https://www.electronicshub.org/raspberry-pi-l298n-interface-tutorial-control-dc-motor-l298n-raspberry-pi/
from getkey import getkey, keys
import RPi.GPIO as GPIO

steer_1 = 25 # pin 22
steer_2 = 8 # pin 24
enA = 7 # pin 26

drive_1 = 16 # pin 36
drive_2 = 20 # pin 38
enB = 21 # pin 40

GPIO.setmode(GPIO.BCM)

pins = [drive_1,drive_2,enA,steer_1,steer_2,enB]

for element in pins:
        GPIO.setup(element,GPIO.OUT) # to set up all GPIO pins
        if element != enA or enB:
                GPIO.output(element,GPIO.LOW) # to set all drive pins low

steer=GPIO.PWM(enA,1000) # '1000' hertz duty cycle
drive=GPIO.PWM(enB,1000)
drive.start(100) # starting the drive motor at a pre-set duty cycle
steer.start(100)

print("\n")
print("To Control: 8 - forward, 2 - backward, 4 - left, 5 - straighten, ")
print("6 - right, e - exit, any other key - stop drive motors")
print("\n")

while True:

        key = getkey()

        if key == '8':
                print("Forward")
                GPIO.output(drive_1,GPIO.LOW)
                GPIO.output(drive_2,GPIO.HIGH)
        elif key == '2':
                print("Backward")
                GPIO.output(drive_1,GPIO.HIGH)
                GPIO.output(drive_2,GPIO.LOW)
        elif key == '4':
                print("Turning Left")
                GPIO.output(steer_1,GPIO.LOW)
                GPIO.output(steer_2,GPIO.HIGH)
        elif key == '5':
                print("Straightening Out")
                GPIO.output(steer_1,GPIO.LOW)
                GPIO.output(steer_2,GPIO.LOW)
        elif key == '6':
                print("Turning Right")
                GPIO.output(steer_1,GPIO.HIGH)
                GPIO.output(steer_2,GPIO.LOW)
        elif key == 'e':
                print("Cleaning up and exiting")
                GPIO.cleanup()
                break
        elif key != '8' or '2' or '4' or '5' or '6':
                GPIO.output(drive_1,GPIO.LOW)
                GPIO.output(drive_2,GPIO.LOW)
