import TCRead
import datetime
import pandas as pd

runtime = 60
i = 0

end_time = datetime.datetime.now()+ datetime.timedelta(0,runtime)

datatable = [datetime.datetime.now()]
datatable.append(runtime)
datatable.append("||")

while datetime.datetime.now() < end_time:
    datatable.append(TCRead.get_temp())

print(datatable)

def create_csv(e):
    file_name = r"C:\Users\John\Desktop\"" \
                 + e + ".csv"
    df = pd.DataFrame(datatable)
    df.to_csv(file_name, index=False)