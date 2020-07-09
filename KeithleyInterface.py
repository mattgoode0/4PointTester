"""
Reference programming manual:
https://www.tek.com/keithley-source-measure-units/keithley-smu-2400-graphical-series-sourcemeter-manual-8
"""

import pyvisa  # https://pyvisa.readthedocs.io/en/1.5-docs/instruments.html
import TCRead


class FourPointProbe:

    def __init__(self, name, startV, endV, steps, wait, mode, units, sweep_type):
        # Open connection to Keithley Unit
        self.rm = pyvisa.ResourceManager()
        print(self.rm.list_resources())
        self.instrument = self.rm.open_resource('USB::0x05E6::0x2460::04446789::INSTR')
        print('Connected to 2460 High-Current Source Meter')

        self.instrument.write("*RST")
        self.instrument.write("SOUR:FUNC " + units)  # Set the source function to specified unit.
        self.instrument.write("SYSTEM:" + mode)  # sets scope to 2 or 4 wire
        self.instrument.write("SOUR:" + units + ":RANG AUTO")  # Set the source range to 20 V.
        self.instrument.write("SOUR:" + units + ":VLIM 20")  # Set the source limit for measurements to

        if units == "CURRent":
            self.instrument.write("SENS:FUNC \"VOLT\"")  # Set the measure function to voltage.
            self.instrument.write("SENS:VOLT:RANG AUTO")  # Set the current range to automatic
        else:
            self.instrument.write("SENS:FUNC \"CURRent\"")  # Set the measure function to Current.
            self.instrument.write("SENS:CURRent:RANGe:AUTO")  # Set the current range to automatic

        self.instrument.write(
            "SOUR:SWE:CURR:LOG 100e-3, 6, 100, 100e-3, 1, BEST, OFF")  # Set up a linear sweep that sweeps from
        # 0 to 10 V in 21 steps with a source delay of 200 ms.

        self.instrument.write("SOUR:SWE:" + units + ":" + sweep_type + " " + startV + ", " + endV + ", " + steps + ", "
                              + wait + ", 1, BEST, OFF")
        TCRead.get_temp(True)
        self.instrument.write("INIT; *WAI")
        self.instrument.write("TRAC:DATA? 1, 100, \"defbuffer1\", SOUR, READ")
        savedata = "TRAC:SAVE \"/usb1/myData" + str(name) + ".csv\", \"defbuffer1\""
        self.instrument.write(savedata)
        TCRead.get_temp(False)
        print("Data Saved")

    def disconnect(self):
        self.instrument.close()
