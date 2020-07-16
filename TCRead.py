import serial
import datetime
import time
import pandas as pd

# Define the serial port and baud rate.
# Ensure the 'COM#' corresponds to what was seen in the Windows Device Manager
ser = serial.Serial('COM7', 9600)


def get_temp(steps, wait, name):
    time.sleep(1)  # waits for 1 second as the buzzer beeps for 1 second to signal start of test
    data_storage = [datetime.datetime.now()]
    data_storage.append('Steps: ' + str(steps))
    data_storage.append('Wait time: ' + str(wait))
    i = 1

    # record TC at each step of the sweep
    while i <= int(steps):
        raw_temp = str(ser.readline())
        temp = i + "," + float(raw_temp[2:7])
        data_storage.append(temp)
        time.sleep(int(wait))
        i += 1

    df = pd.DataFrame(data_storage)
    file_name = 'SAMPLETC_' + str(name) + '.csv'
    df.to_csv(file_name, index=False)
