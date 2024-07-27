import Adafruit_BBIO.GPIO as GPIO
import Adafruit_BBIO.ADC as ADC
from time import sleep
ADC.setup()

# Set up pins as inputs or outputs
GPIO.setup("P9_23", GPIO.OUT)
GPIO.setup("P9_27", GPIO.OUT)
GPIO.output("P9_23", GPIO.LOW)
GPIO.output("P9_27", GPIO.LOW)
sleep(0.1)
sumvolt = 0
rawsumvolt = 0

for i in range(0,5):
        value=0
        voltage=0
        rawvoltage=0 
        rawvalue=0
        # Write a logic high or logic low
        GPIO.output("P9_23", GPIO.HIGH)
        GPIO.output("P9_27", GPIO.LOW)
        sleep(0.000009)
    
        value = ADC.read("P9_39")
        voltage = value*1.8
        rawvalue = ADC.read_raw("P9_39")
        rawvoltage = (rawvalue*1.8)/4096
        print("normal voltage",voltage)
        rawsumvolt += rawvoltage    
        sumvolt += voltage
        #sleep(3)
        GPIO.output("P9_23",GPIO.LOW)
        sleep(0.01)
        #sleep(60)
        
GPIO.cleanup()

#print("raw sum voltage=",rawsumvolt)
#print("sum voltage=",sumvolt)

rawsensor_volt = rawsumvolt/5
#print("raw sensor voltage = ",rawsensor_volt)
rawresistance = (510*(3.3-rawsensor_volt)/rawsensor_volt)
#print("raw resistance = ",rawresistance)


sensor_volt = sumvolt/5
#print("sensor voltage = ",sensor_volt)
resistance = (510*(3.3-sensor_volt)/sensor_volt)
total_resistance = (resistance + rawresistance)/2
#print("resistance = ",total_resistance)

if total_resistance>400 and total_resistance<1500:	
	print("VERY WET and Resistance=",total_resistance,"Ohm")
elif total_resistance>1500 and total_resistance<5000:	
	print("MODERATE WET and Resistance=",total_resistance,"Ohm")
elif total_resistance>5000:	
	print("VERY DRY	and Resistance=",total_resistance,"Ohm")


