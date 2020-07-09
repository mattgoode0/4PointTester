#import TCRead
#import KeithleyInterface
import time
import trial_class

start_time = time.time()

print("connected")
#print(TCRead.get_temp())
#print(TCRead.get_temp())
#print("--- %s seconds ---" % (time.time() - start_time))

time.sleep(2)
print("measurment 3")
#print(TCRead.get_temp())
#print("--- %s seconds ---" % (time.time() - start_time))

file_name = "SampleG17L"

# KeithleyInterface.FourPointProbe()
# KeithleyInterface.FourPointProbe.start_testing(True, file_name)

trial_class.TestClass()
trial_class.TestClass.second_round(file_name, start_time)