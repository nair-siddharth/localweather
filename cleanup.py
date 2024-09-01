import sqlite3
from datetime import datetime, timedelta

# Connect to SQLite database
conn = sqlite3.connect('/home/dietpi/sensor_data.db')
cursor = conn.cursor()

# Function to delete records older than 30 days
def cleanup_old_data():
    thirty_days_ago = datetime.now() - timedelta(days=300)
    cursor.execute("DELETE FROM sensor_readings WHERE timestamp < ?", (thirty_days_ago,))
    conn.commit()

if __name__ == "__main__":
    cleanup_old_data()
    conn.close()
