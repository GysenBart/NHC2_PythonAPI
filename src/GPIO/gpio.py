import RPi.GPIO as GPIO

class GPIOController:
    def __init__(self, mode=GPIO.BCM):
        self.mode = mode
        GPIO.setmode(mode)
        
    def setup_pin(self, pin, direction, pull_up_down=GPIO.PUD_OFF):
        GPIO.setup(pin, direction, pull_up_down)
        
    def set_output(self, pin, state):
        GPIO.output(pin, state)
        
    def get_input(self, pin):
        return GPIO.input(pin)
    
    def add_event(self, pin, edge, callback, bouncetime=200):
        """
        Adds event to pin.
        edge: GPIO.RISING, GPIO.FALLING of GPIO.BOTH
        callback: function called when event occours
        bouncetime: a wait time to prevent events bouncing
        """
        GPIO.add_event_detect(pin, edge, callback=callback, bouncetime=bouncetime)

    def cleanup(self):
        GPIO.cleanup()   
