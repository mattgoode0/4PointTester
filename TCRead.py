import serial
import datetime
import time
import pandas as pd

# Define the serial port and baud rate.
# Ensure the 'COM#' corresponds to what was seen in the Windows Device Manager
ser = serial.Serial('COM7', 9600)


def get_temp(steps, wait, name):
    time.sleep(1)  # waits for 1 second as the buzzer beeps for 1 second to singal start of test
    data_storage = [datetime.datetime.now()]
    data_storage.append('Steps: ' + str(steps))
    data_storage.append('Wait time: ' + str(wait))
    runtime = float(steps) * float(wait)
    end_time = datetime.datetime.now() + datetime.timedelta(0, runtime)

    while datetime.datetime.now() < end_time:
        raw_temp = str(ser.readline())
        temp = float(raw_temp[2:7])
        data_storage.append(temp)

    df = pd.DataFrame(data_storage)
    file_name = 'SAMPLE_' + str(name) + '.csv'
    df.to_csv(file_name, index=False)
