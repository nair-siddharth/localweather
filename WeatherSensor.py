import board
import busio
import sqlite3
import time
from adafruit_bmp280 import Adafruit_BMP280_I2C

# Create I2C bus
i2c = busio.I2C(board.SCL, board.SDA)

# Create BMP280 object
bmp280 = Adafruit_BMP280_I2C(i2c, address=0x76)

# Connect to SQLite database
conn = sqlite3.connect('/home/dietpi/sensor_data.db')
cursor = conn.cursor()

# Function to get sensor data and store in database
def log_sensor_data():
    ctr = 0;
    temperature = 0;
    pressure = 0;
    while ctr<100:
        ctr = ctr + 1;
        temperature = temperature  + bmp280.temperature
        pressure = pressure + bmp280.pressure
        time.sleep(.5)

    temperature = temperature/ctr
    pressure = pressure/ctr
    cursor.execute("INSERT INTO sensor_readings (temperature, pressure, timestamp) VALUES (?, ?, datetime('now','localtime'))", (temperature, pressure))
    conn.commit()

if __name__ == "__main__":
    log_sensor_data()
    conn.close()
