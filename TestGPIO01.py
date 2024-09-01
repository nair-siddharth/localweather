import RPi.GPIO as GPIO
import time

# Set up the GPIO mode
GPIO.setmode(GPIO.BCM)

# Define the GPIO pin to use (e.g., GPIO17)
input_pin = 4

# Set up the pin as an input with an internal pull-down resistor
GPIO.setup(input_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

# Define the interrupt callback function
def my_callback(channel):
    print("Interrupt detected on GPIO pin", channel)

# Set up an interrupt on a rising edge (button press, for example)
GPIO.add_event_detect(input_pin, GPIO.RISING, callback=my_callback, bouncetime = 500)

try:
    while True:
        # Main loop can do other tasks while waiting for interrupts
        time.sleep(1)
except KeyboardInterrupt:
    print("Program terminated")

finally:
    # Clean up the GPIO on exit
    GPIO.cleanup()
