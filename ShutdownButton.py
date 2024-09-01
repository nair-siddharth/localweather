import board
import busio
import adafruit_drv2605
import time
import RPi.GPIO as GPIO
import os
import signal

# Create I2C bus
i2c = busio.I2C(board.SCL, board.SDA)

# Initialize DRV2605
drv = adafruit_drv2605.DRV2605(i2c, address = 0x5A)

# Function to trigger a vibration with a specific effect
def trigger_vibration(effect_id):
    drv.sequence[0] = adafruit_drv2605.Effect(effect_id)
    i=0
    while i < 3:
        i = i+1
        time.sleep(3)
        drv.play()
    time.sleep(2)  # Adjust the duration as needed
    drv.stop()

# Use BCM GPIO numbering
GPIO.setmode(GPIO.BCM)

# Set up GPIO 4 (pin 11) as an input with a pull-up resistor
button_pin = 4
GPIO.setup(button_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

def shutdown(channel):
    trigger_vibration(77)
    # Script will end here, and the event detection will run in the background
    # GPIO.cleanup()
    print("Button pressed! Shutting down...")
    time.sleep(.5)
    os.system("sudo shutdown -h now")

# Add event listener on button press (falling edge)
# while True:
#    GPIO.wait_for_edge(button_pin, GPIO.RISING)
#    time.sleep(1)
#    shutdown(button_pin)
time.sleep(0.5)
GPIO.add_event_detect(button_pin, GPIO.RISING, callback=shutdown, bouncetime=200)
signal.pause()
