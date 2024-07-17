import serial
import time
from datetime import datetime
import os
import pandas as pd

def read_arduino():
    arduino_port = "/dev/ttyACM0"
    if arduino_port is None:
        print("No Arduino found!")
        return

    baud = 115200  # set the baud rate as per your Arduino code

    csv_path = os.path.join(os.path.dirname(__file__), 'data/data_log.csv')

    # Ensure the directory exists
    os.makedirs(os.path.dirname(csv_path), exist_ok=True)

    # Check if the CSV file exists, create it with headers if it does not
    if not os.path.isfile(csv_path):
        df = pd.DataFrame(columns=["ppm", "datetime", "quality"])
        df.to_csv(csv_path, index=False)

    ser = serial.Serial(arduino_port, baud)

    print("Connecting to Arduino port ...")
    time.sleep(2)

    print("Connected to Arduino port:" + arduino_port)
    time.sleep(1)

    file_exists = os.path.isfile(csv_path)

    print("Reading the data ...")

    while True:
        with open(csv_path, "a") as file:
            # Get the current time
            current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            # Read a line and convert it from b'xxx\r\n' to xxx
            getData = str(ser.readline())
            data = getData[2:][:-5]
            data = data.split(':')[-1].split('ppm')[0]
            if data == '' or data == 'pm':
                data = '0'

            ppm_value = int(data)

            # Quality column condition
            if ppm_value < 50:
                quality = 'ERROR no contact with water'
            elif 50 <= ppm_value <= 150:
                quality = 'Excellent for drinking'
            elif 150 < ppm_value <= 250:
                quality = 'Good'
            elif 250 < ppm_value <= 300:
                quality = 'Fair'
            else:
                quality = 'Poor not good for drinking'

            print("=" * 70)
            print(f"{ppm_value}, {current_time}, {quality}")
            print("=" * 70)

            # Write data with timestamp
            file.write(f"{ppm_value},{current_time},{quality}\n")

            # Wait for 1 second before the next read
            time.sleep(1)

if __name__ == '__main__':
    read_arduino()
