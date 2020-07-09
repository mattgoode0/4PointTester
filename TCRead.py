import serial
import datetime
import pandas as pd

# Define the serial port and baud rate.
# Ensure the 'COM#' corresponds to what was seen in the Windows Device Manager
#ser = serial.Serial('COM7', 9600)


def get_temp(i):
    data_storage = [datetime.datetime.now()]
    while i:
        raw_temp = str(ser.readline())
        temp = float(raw_temp[2:7])
        data_storage.append(temp)
    data_storage.append(datetime.datetime.now())
    return data_storage

    df = pd.DataFrame(data_storage)
    df.to_csv('UV_Data.csv', index=False)
