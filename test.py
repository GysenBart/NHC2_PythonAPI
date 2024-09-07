from src.GPIO.gpio import GPIOController

print("Hello RPI")

try:
    import RPi.GPIO as GPIO
except RuntimeError:
    print("Error importing RPi.GPIO!  This is probably because you need superuser privileges.  You can achieve this by using 'sudo' to run your script")
    
gpio = GPIOController()

gpio.setup_pin(1, GPIO.OUT)
gpio.set_output(1, 1)

input(print('Press a key to set the relay'))

gpio.set_output(1, 0)

input(print('Press a key to set the relay'))

gpio.set_output(1, 1)