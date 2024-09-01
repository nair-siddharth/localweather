import board
import busio
import adafruit_drv2605
import time

# Create I2C bus
i2c = busio.I2C(board.SCL, board.SDA)

# Initialize DRV2605
drv = adafruit_drv2605.DRV2605(i2c, address = 0x5A)

# Function to trigger a vibration with a specific effect
def trigger_vibration(effect_id):
    drv.sequence[0] = adafruit_drv2605.Effect(effect_id)
    drv.play()
    time.sleep(2)  # Adjust the duration as needed
    drv.stop()

if __name__ == "__main__":
    # Example: Trigger effect with ID 1 (you can change this to try other effects)
    trigger_vibration(int(input('Enter Effect id (1-123) - ')))
    i=0;
    while i<123:
        i=i+1;
        print('Effect# ', end = '--> ')
        print(i)
        trigger_vibration(i);
