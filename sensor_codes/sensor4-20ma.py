import Adafruit_BBIO.ADC as ADC
from time import sleep
ADC.setup()
temp = ADC.read("P9_36") 
hum = ADC.read("P9_35")
temp_raw = (ADC.read_raw("P9_36"))*1.8/4096
hum_raw  = (ADC.read_raw("P9_35"))*1.8/4096
#print("raw temp",temp_raw)
#print("raw hum",hum_raw) 
temp1 = temp*1.8
hum1 = hum*1.8
print("voltage temp",temp1)
print("voltage hum",hum1)
temp2 = (temp1/75)*1000
hum2 = (hum1/75)*1000
temperature = (temp2-4)*10 - 45
humidity = (hum2-4)*6.25
print("Temperature=",temperature,"Degree Celsius") 
print("Humidity=",humidity,"%") 
