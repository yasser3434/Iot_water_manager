import serial
import time
from datetime import datetime
import os

def read_arduino():
    # Replace '/dev/ttyACM0' with your Arduino's serial port
    arduino_port = "/dev/ttyACM1"
    baud = 115200  # set the baud rate as per your Arduino code
    filename = "data/data_log.csv"  # name of the file to save data

    ser = serial.Serial(arduino_port, baud)

    print("Connecting to Arduino port ...")
    time.sleep(2)

    print("Connected to Arduino port:" + arduino_port)
    time.sleep(1)

    file_exists = os.path.isfile(filename)

    quality = ''

    if not file_exists:
        with open(filename, "a") as file:
            file.write("ppm,datetime,quality\n")  # Writing header for CSV file
            print("File created")
            file.close()
    else:
        print("Appending to existing file")

    print("Reading the data ...")

    while True:
        with open(filename, "a") as file:

            # Get the current time
            current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            # Read a line and convert it from b'xxx\r\n' to xxx
            getData = str(ser.readline())
            data = getData[2:][:-5]
            data = data.split(':')[-1].split('ppm')[0]
            if data == '' or data == 'pm':
                data = '0'

            ppm_value = int(data)
            # ppm_value = int(float(data.split(':')[-1].split('ppm')[0]))

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

            print(f"{ppm_value}, {current_time}, {quality}")

            # Write data with timestamp
            file.write(f"{ppm_value},{current_time},{quality}\n")

            # Wait for 1 second before the next read
            time.sleep(1)

if __name__ == '__main__':
    read_arduino()
