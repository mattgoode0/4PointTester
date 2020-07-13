"""
Reference programming manual:
https://www.tek.com/keithley-source-measure-units/keithley-smu-2400-graphical-series-sourcemeter-manual-8
"""

import pyvisa  # https://pyvisa.readthedocs.io/en/1.5-docs/instruments.html
import TCRead
import datetime


class FourPointProbe:

    def __init__(self, name, startV, endV, steps, wait, mode, units, sweep_type):
        # Open connection to Keithley Unit
        self.rm = pyvisa.ResourceManager()
        print(self.rm.list_resources())
        self.instrument = self.rm.open_resource('USB::0x05E6::0x2460::04446789::INSTR')
        print('Connected to 2460 High-Current Source Meter')

        del self.instrument.timeout

        self.instrument.write("*RST")
        self.instrument.write("SOUR:FUNC " + mode)  # Set the source function to specified unit.
        self.instrument.write("SYSTEM:" + units)  # sets scope to 2 or 4 wire
        self.instrument.write("SOUR:" + mode + ":RANG " + endV)  # Set the source range to 20 V.

        if mode == "CURRent":
            self.instrument.write("SOUR:CURR:VLIM 105")  # Set the source limit for measurements to
            self.instrument.write("SENS:FUNC \"VOLT\"")  # Set the measure function to voltage.
            self.instrument.write("SENS:VOLT:RANGe:AUTO ON")  # Set the current range to automatic
        else:
            self.instrument.write("SOUR:VOLT:ILIM 7.3")
            self.instrument.write("SENS:FUNC \"CURRent\"")  # Set the measure function to Current.
            self.instrument.write("SENS:CURRent:RANGe:AUTO ON")  # Set the current range to automatic

        self.instrument.write("SOUR:SWE:" + mode + ":" + sweep_type + " " + startV + ", " + endV + ", " + steps + ", "
                              + wait + ", 1, BEST, OFF")

        self.instrument.write(":SYSTem:BEEPer 500, 1")
        self.instrument.write("INIT;*WAI")
        self.instrument.write(":SYSTem:BEEPer 500, 1")
        print(datetime.datetime.now())
        TCRead.get_temp(steps, wait, name)


        savedata = "TRAC:SAVE \"/usb1/SAMPLE_" + str(name) + ".csv\", \"defbuffer1\""
        self.instrument.write(savedata)
        print("Data Saved")
        print(datetime.datetime.now())
        self.disconnect()

    def disconnect(self):
        self.instrument.close()
