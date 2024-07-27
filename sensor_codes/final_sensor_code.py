import serial
import time
import binascii
#ser = serial.Serial(port = "/dev/ttyUSB0",baudrate=9600,timeout=1)


def get_temp_hex():
 string_temp = '01030013000175CF'
 #byte_message = ([0x31, 0x32, 0x33, 0x34, 0x35, 0x36, 0x37]);
 send_temp=bytes.fromhex(string_temp)
 ser.write(send_temp)
 response_bytes_temp=ser.read(12).hex()
 print("received hex:",response_bytes_temp)
 hex_value1=response_bytes_temp
 temp_final_return=extract_hex_temp(hex_value1)
 return temp_final_return
#time.sleep(6)
"""
while True:
   if ser.in_waiting > 0:
      data=ser.read(20)
      print(data)
"""
#time.sleep(8)
"""
while True:
  bytesToRead = ser.inWaiting()
  data=ser.read(bytesToRead)
"""
#print(data)

#response_bytes_temp=ser.read(12).hex()
#print("received hex:",response_bytes_temp)
#print("received hex:",response_bytes_moisture)
#print("received hex:",response_bytes_ec)

#time.sleep(0.4)
def get_moisture_hex():
 string_moisture='010300120001240F'
 send_moisture=bytes.fromhex(string_moisture)
 ser.write(send_moisture)
 response_bytes_moisture=ser.read(12).hex()
 print("received hex:",response_bytes_moisture)
 hex_value2=response_bytes_moisture
 moisture_final_return=extract_hex_moisture(hex_value2)
 return moisture_final_return
#time.sleep(0.4)

def get_ec_hex():
 string_ec='01030015000195CE'
 send_ec=bytes.fromhex(string_ec)
 ser.write(send_ec)
 response_bytes_ec=ser.read(12).hex()
 print("received hex:",response_bytes_ec)
 hex_value3=response_bytes_ec
 ec_final_return=extract_hex_ec(hex_value3)
 return ec_final_return
#time.sleep(0.4)

""" get hex value from sensor"""
#hex_value1=response_bytes_temp
#hex_value2=response_bytes_moisture
#hex_value3=response_bytes_ec
#integer_value=int(hex_value,16)
#print(integer_value)

#first_byte=(integer_value >> 24) & 0xFF

#print("first byte",hex(first_byte))
#byte_data=bytearray.fromhex(hex_value)


"""extracting particular byte for calculation of 
                                  humidity,temp,conductivity"""
#index_to_extract=3
#index_to_extract1=4


#index_to_extract2=5
#index_to_extract3=6
def extract_hex_temp(hex_value1):
    index_to_extract=3
    index_to_extract1=4
    extracted_hex_temp1=hex_value1[index_to_extract*2:(index_to_extract + 1)*2]
    extracted_hex_temp2=hex_value1[index_to_extract1*2:(index_to_extract1 + 1)*2]
    temp_hex=extracted_hex_temp1+extracted_hex_temp2
    temp_int_value=int(temp_hex,16)
    temp_final=temp_int_value/10
   # print(temp_final)
    print(temp_hex)
    print("Soil Temperature Detected--------->",temp_final,"Degree celsius")
    return temp_final 

def extract_hex_moisture(hex_value2):
    index_to_extract=3
    index_to_extract1=4
    extracted_hex_moisture1=hex_value2[index_to_extract*2:(index_to_extract + 1)*2]
    extracted_hex_moisture2=hex_value2[index_to_extract1*2:(index_to_extract1 + 1)*2]
    moisture_hex=extracted_hex_moisture1+extracted_hex_moisture2
    moisture_int_value=int(moisture_hex,16)
    moisture_final=moisture_int_value/10
    print(moisture_hex)
    print("Soil Humidity Detected(%) --------->",moisture_final,"RH")
    return moisture_final


def extract_hex_ec(hex_value3):
    index_to_extract=3
    index_to_extract1=4
    extracted_hex_ec1=hex_value3[index_to_extract*2:(index_to_extract + 1)*2]
    extracted_hex_ec2=hex_value3[index_to_extract1*2:(index_to_extract1 + 1)*2]
    ec_hex=extracted_hex_ec1+extracted_hex_ec2
    ec_int_value=int(ec_hex,16)
    ec_final=ec_int_value
    print(ec_hex)
    print("soil Conductivity Detected-------->",ec_final,"us/cm")
    return ec_final
""" coverting hex values to decimal """
#temp_int_value=int(temp_hex,16)
#moisture_int_value=int(moisture_hex,16)
#ec_int_value=int(ec_hex,16)

#print(temp_int_value)
#print(moisture_int_value)
#print(ec_int_value)

""" final values of sensor"""
#temp_final=temp_int_value/10
#moisture_final=moisture_int_value/10
#ec_final=ec_int_value

#print("Soil Temperature Detected--------->",temp_final,"Degree celsius")
#print("Soil Humidity Detected(%) --------->",moisture_final,"RH")
#print("soil Conductivity Detected-------->",ec_final,"us/cm")


#ec_final_string=str(ec_final)
#ec_String="\"ec_final_string\""
#def generate_at_string():
# temp_final_string=f"AT+send=\"TEMPERATURE--->{temp_final}\""
# moisture_final_string=f"AT+send=\"Humidity--->{moisture_final}\""
# ec_final_string=f"AT+send=\"Conductivity--->{ec_final}\""
# temp_command=temp_final_string
# moisture_command=moisture_final_string
# ec_command=ec_final_string
 
#ser.close()

ser1 = serial.Serial(port = "/dev/ttyO5",baudrate=115200,timeout=1)

def join_func():
   # ser1 = serial.Serial(port = "/dev/ttyO4",baudrate=115200,timeout=1)
    while True:
      command="AT+JOIN"
      #time.sleep(0.5)
      #ser1.write(command.encode('utf-8'))
      time.sleep(0.5)
      ser1.write(command.encode('utf-8')+b"\r\n")
      time.sleep(0.5)
      response=ser1.readline().decode('utf-8').strip()
      #response=ser1.read(50)
      print("response--->",response)
      time.sleep(1)
      response1=ser1.readline().decode('utf-8').strip()
#response1=ser1.read(50)
      print("response1---->",response1)
      if response == "+JOIN: JOIN_ACCEPTED":
       time.sleep(0.5)
       break;
 # elif response == "+JOIN: JOIN_ACCEPTED":
     # time.sleep(0.5) 
     # break;
#command1="AT+SEND="+ec_String+"\r\n"
#command="AT"
def send_ec_func(ec_command):
    while 1:
      ser1.write(ec_command.encode('utf-8')+b"\r\n")
      time.sleep(0.5)
      response2=ser1.readline().decode('utf-8').strip()
      #response2=ser1.read(20)
      print("ec1_response--->",response2)
      time.sleep(1)
      #response3=ser1.read(20)
      response3=ser1.readline().decode('utf-8').strip()
      print("ec2_response--->",response3)
      if response2 == "+SEND: OK":
        time.sleep(0.5)
        break;
      elif response3 == "+SEND: NO_NETWORK_JOINED":
        time.sleep(0.5) 
        join_func()

def send_temp_func(temp_command):
    while 1:
      ser1.write(temp_command.encode('utf-8')+b"\r\n")
      time.sleep(0.5)
      temp_response=ser1.readline().decode('utf-8').strip()
      print("temp_response",temp_response)
      time.sleep(1)
      temp1_response=ser1.readline().decode('utf-8').strip()
      print("temp1_response",temp1_response)
      if temp_response == "+SEND: OK":
        time.sleep(0.5)
        break;
      elif temp1_response == "+SEND: NO_NETWORK_JOINED":
        time.sleep(0.5) 
        join_func()

def send_humidity_func(moisture_command):
    while 1:
      ser1.write(moisture_command.encode('utf-8')+b"\r\n")
      time.sleep(0.5)
      moisture_response=ser1.readline().decode('utf-8').strip()
      print("moisture_Response-->",moisture_response)
      time.sleep(0.5)
      moisture1_response=ser1.readline().decode('utf-8').strip()
      print("moisturee1_Response--->",moisture1_response)
      if moisture_response == "+SEND: OK":
        time.sleep(0.5)
        break;

def send_alldata_func(send_alldata_command):
    while 1:
      ser1.write(send_alldata_command.encode('utf-8')+b"\r\n")
      time.sleep(0.5)
      alldata_response=ser1.readline().decode('utf-8').strip()
      print("alldata_Response-->",alldata_response)
      time.sleep(0.5)
      alldata1_response=ser1.readline().decode('utf-8').strip()
      print("alldata1_Response--->",alldata1_response)
      if alldata_response == "+SEND: OK":
        time.sleep(0.5)
        break;



def utility_func():
    ser = serial.Serial(port = "/dev/ttyO4",baudrate=9600,timeout=1)
    temp_final_return=get_temp_hex()
    print(temp_final_return)
    time.sleep(0.4)
    moisture_final_return=get_moisture_hex()
    time.sleep(0.4)
    ec_final_return=get_ec_hex()
    time.sleep(0.4)
    temp_final_string=f"AT+send=\"TEMPERATURE--->{temp_final_return}\""
    moisture_final_string=f"AT+send=\"Humidity--->{moisture_final_return}\""
    ec_final_string=f"AT+send=\"Conductivity--->{ec_final_return}\""
    send_alldata=f"AT+send=\"TEMP-->{temp_final_return}--Hum-->{moisture_final_return}--Conductivity-->{ec_final_return}\""

    temp_command=temp_final_string
    moisture_command=moisture_final_string
    ec_command=ec_final_string
    send_alldata_command=send_alldata

    #ser.close()
    time.sleep(0.2)
    #send_alldata_func(send_alldata_command)
   # send_temp_func(temp_command)
   # time.sleep(0.2)

    #send_humidity_func(moisture_command)
    #time.sleep(0.2)
    
    #send_ec_func(ec_command)
    #time.sleep(0.2)
    send_alldata_func(send_alldata_command)




ser = serial.Serial(port = "/dev/ttyO4",baudrate=9600,timeout=1)
temp_final_return=get_temp_hex()
print(temp_final_return)
time.sleep(0.4)
moisture_final_return=get_moisture_hex()
time.sleep(0.4)
ec_final_return=get_ec_hex()
time.sleep(0.4)
temp_final_string=f"AT+send=\"TEMPERATURE--->{temp_final_return}\""
moisture_final_string=f"AT+send=\"Humidity--->{moisture_final_return}\""
ec_final_string=f"AT+send=\"Conductivity--->{ec_final_return}\""
send_alldata=f"AT+send=\"TEMP-->{temp_final_return}--Hum-->{moisture_final_return}--Cond-->{ec_final_return}\""
temp_command=temp_final_string
moisture_command=moisture_final_string
ec_command=ec_final_string
send_alldata_command=send_alldata
#ser.close()
join_func()
time.sleep(0.2)
send_temp_func(temp_command)
time.sleep(0.2)
send_humidity_func(moisture_command)
time.sleep(0.2)
send_ec_func(ec_command)
time.sleep(0.2)
send_alldata_func(send_alldata_command)

while 1:
 utility_func()
 print("\nWaiting to fetch Real time data................")
 time.sleep(9)

ser1.close()
