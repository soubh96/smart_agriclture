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

def get_moisture_hex():
 string_moisture='010300120001240F'
 send_moisture=bytes.fromhex(string_moisture)
 ser.write(send_moisture)
 response_bytes_moisture=ser.read(12).hex()
 print("received hex:",response_bytes_moisture)
 hex_value2=response_bytes_moisture
 moisture_final_return=extract_hex_moisture(hex_value2)
 return moisture_final_return

def get_ec_hex():
 string_ec='01030015000195CE'
 send_ec=bytes.fromhex(string_ec)
 ser.write(send_ec)
 response_bytes_ec=ser.read(12).hex()
 print("received hex:",response_bytes_ec)
 hex_value3=response_bytes_ec
 ec_final_return=extract_hex_ec(hex_value3)
 return ec_final_return
 
def get_ph_hex():
 string_ph = '010300060001640B'
 #byte_message = ([0x31, 0x32, 0x33, 0x34, 0x35, 0x36, 0x37]);
 send_ph=bytes.fromhex(string_ph)
 ser.write(send_ph)
 response_bytes_ph=ser.read(12).hex()
 print("received hex:",response_bytes_ph)
 hex_value1=response_bytes_ph
 ph_final_return=extract_hex_ph(hex_value1)
 return ph_final_return
 
def get_nitro_hex():
 string_nitro = '0103001E0001E40C'
 #byte_message = ([0x31, 0x32, 0x33, 0x34, 0x35, 0x36, 0x37]);
 send_nitro=bytes.fromhex(string_nitro)
 ser.write(send_nitro)
 response_bytes_nitro=ser.read(12).hex()
 print("received hex:",response_bytes_nitro)
 hex_value1=response_bytes_nitro
 nitro_final_return=extract_hex_nitro(hex_value1)
 return nitro_final_return

def get_phos_hex():
 string_phos = '0103001F0001B5CC'
 #byte_message = ([0x31, 0x32, 0x33, 0x34, 0x35, 0x36, 0x37]);
 send_phos=bytes.fromhex(string_phos)
 ser.write(send_phos)
 response_bytes_phos=ser.read(12).hex()
 print("received hex:",response_bytes_phos)
 hex_value1=response_bytes_phos
 phos_final_return=extract_hex_phos(hex_value1)
 return phos_final_return

def get_pot_hex():
 string_pot = '01030020000185C0'
 #byte_message = ([0x31, 0x32, 0x33, 0x34, 0x35, 0x36, 0x37]);
 send_pot=bytes.fromhex(string_pot)
 ser.write(send_pot)
 response_bytes_pot=ser.read(12).hex()
 print("received hex:",response_bytes_pot)
 hex_value1=response_bytes_pot
 pot_final_return=extract_hex_pot(hex_value1)
 return pot_final_return







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
    ec_final=ec_int_value/10
    print(ec_hex)
    print("Soil Conductivity Detected-------->",ec_final,"us/cm")
    return ec_final
  
def extract_hex_ph(hex_value3):
    index_to_extract=3
    index_to_extract1=4
    extracted_hex_ph1=hex_value3[index_to_extract*2:(index_to_extract + 1)*2]
    extracted_hex_ph2=hex_value3[index_to_extract1*2:(index_to_extract1 + 1)*2]
    ph_hex=extracted_hex_ph1+extracted_hex_ph2
    ph_int_value=int(ph_hex,16)
    ph_final=ph_int_value/100
    print(ph_hex)
    print("Soil PH Detected-------->",ph_final,"PH")
    return ph_final

def extract_hex_nitro(hex_value3):
    index_to_extract=3
    index_to_extract1=4
    extracted_hex_nitro1=hex_value3[index_to_extract*2:(index_to_extract + 1)*2]
    extracted_hex_nitro2=hex_value3[index_to_extract1*2:(index_to_extract1 + 1)*2]
    nitro_hex=extracted_hex_nitro1+extracted_hex_nitro2
    nitro_int_value=int(nitro_hex,16)
    nitro_final=nitro_int_value
    print(nitro_hex)
    print("Soil Nitrogen Detected-------->",nitro_final,"mg/kg")
    return nitro_final
    
def extract_hex_phos(hex_value3):
    index_to_extract=3
    index_to_extract1=4
    extracted_hex_phos1=hex_value3[index_to_extract*2:(index_to_extract + 1)*2]
    extracted_hex_phos2=hex_value3[index_to_extract1*2:(index_to_extract1 + 1)*2]
    phos_hex=extracted_hex_phos1+extracted_hex_phos2
    phos_int_value=int(phos_hex,16)
    phos_final=phos_int_value
    print(phos_hex)
    print("Soil Phosphorus Detected-------->",phos_final,"mg/kg")
    return phos_final

def extract_hex_pot(hex_value3):
    index_to_extract=3
    index_to_extract1=4
    extracted_hex_pot1=hex_value3[index_to_extract*2:(index_to_extract + 1)*2]
    extracted_hex_pot2=hex_value3[index_to_extract1*2:(index_to_extract1 + 1)*2]
    pot_hex=extracted_hex_pot1+extracted_hex_pot2
    pot_int_value=int(pot_hex,16)
    pot_final=pot_int_value
    print(pot_hex)
    print("Soil Potassium Detected-------->",pot_final,"mg/kg")
    return pot_final


ser1 = serial.Serial(port = "/dev/ttyO5",baudrate=115200,timeout=1)

def join_func():
   #ser1 = serial.Serial(port = "/dev/ttyO5",baudrate=115200,timeout=1)
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
      print("moisture1_Response--->",moisture1_response)
      if moisture_response == "+SEND: OK":
        time.sleep(0.5)
        break;
      elif moisture_response == "+SEND: NO_NETWORK_JOINED":
        time.sleep(0.5) 
        join_func()

def send_ph_func(ph_command):
    while 1:
      ser1.write(ph_command.encode('utf-8')+b"\r\n")
      time.sleep(0.5)
      ph_response=ser1.readline().decode('utf-8').strip()
      print("ph_response",ph_response)
      time.sleep(1)
      ph_response=ser1.readline().decode('utf-8').strip()
      print("ph_response",ph1_response)
      if ph_response == "+SEND: OK":
        time.sleep(0.5)
        break;
      elif ph1_response == "+SEND: NO_NETWORK_JOINED":
        time.sleep(0.5) 
        join_func()

def send_nitro_func(nitro_command):
    while 1:
      ser1.write(nitro_command.encode('utf-8')+b"\r\n")
      time.sleep(0.5)
      nitro_response=ser1.readline().decode('utf-8').strip()
      print("nitro_response",nitro_response)
      time.sleep(1)
      nitro1_response=ser1.readline().decode('utf-8').strip()
      print("nitro1_response",nitro1_response)
      if nitro_response == "+SEND: OK":
        time.sleep(0.5)
        break;
      elif nitro1_response == "+SEND: NO_NETWORK_JOINED":
        time.sleep(0.5) 
        join_func()

def send_phos_func(phos_command):
    while 1:
      ser1.write(phos_command.encode('utf-8')+b"\r\n")
      time.sleep(0.5)
      phos_response=ser1.readline().decode('utf-8').strip()
      print("phos_response",phos_response)
      time.sleep(1)
      phos1_response=ser1.readline().decode('utf-8').strip()
      print("phos1_response",phos1_response)
      if phos_response == "+SEND: OK":
        time.sleep(0.5)
        break;
      elif phos1_response == "+SEND: NO_NETWORK_JOINED":
        time.sleep(0.5) 
        join_func()

def send_pot_func(pot_command):
    while 1:
      ser1.write(pot_command.encode('utf-8')+b"\r\n")
      time.sleep(0.5)
      pot_response=ser1.readline().decode('utf-8').strip()
      print("pot_response",pot_response)
      time.sleep(1)
      pot1_response=ser1.readline().decode('utf-8').strip()
      print("pot1_response",pot1_response)
      if pot_response == "+SEND: OK":
        time.sleep(0.5)
        break;
      elif pot1_response == "+SEND: NO_NETWORK_JOINED":
        time.sleep(0.5) 
        join_func()



def utility_func():
    ser = serial.Serial(port = "/dev/ttyO4",baudrate=9600,timeout=1)
    temp_final_return=get_temp_hex()
    print(temp_final_return)
    time.sleep(0.4)
    moisture_final_return=get_moisture_hex()
    time.sleep(0.4)
    ec_final_return=get_ec_hex()
    time.sleep(0.4)
    ph_final_return=get_ph_hex()
    time.sleep(0.4)
    nitro_final_return=get_nitro_hex()
    time.sleep(0.4)
    phos_final_return=get_phos_hex()
    time.sleep(0.4)
    pot_final_return=get_pot_hex()
    time.sleep(0.4)
    
    temp_final_string=f"AT+send=\"TEMPERATURE--->{temp_final_return}\""
    moisture_final_string=f"AT+send=\"Humidity--->{moisture_final_return}\""
    ec_final_string=f"AT+send=\"Conductivity--->{ec_final_return}\""
    ph_final_string=f"AT+send=\"PH--->{ph_final_return}\""
    nitro_final_string=f"AT+send=\"Nirogen--->{nitro_final_return}\""
    phos_final_string=f"AT+send=\"Phosphorus--->{phos_final_return}\""
    pot_final_string=f"AT+send=\"Potassium--->{pot_final_return}\""
        
    temp_command=temp_final_string
    moisture_command=moisture_final_string
    ec_command=ec_final_string
    ph_command=ph_final_string
    nitro_command=nitro_final_string
    phos_command=phos_final_string
    pot_command=pot_final_string
    
    #ser.close()
    time.sleep(0.2)
    send_temp_func(temp_command)
    time.sleep(0.2)
    send_humidity_func(moisture_command)
    time.sleep(0.2)
    send_ec_func(ec_command)
    time.sleep(0.2)
    send_ph_func(ph_command)
    time.sleep(0.2)
    send_nitro_func(nitro_command)
    time.sleep(0.2)
    send_phos_func(phos_command)
    time.sleep(0.2)
    send_pot_func(pot_command)





ser = serial.Serial(port = "/dev/ttyO4",baudrate=9600,timeout=1)

temp_final_return=get_temp_hex()
print(temp_final_return)
time.sleep(0.4)
moisture_final_return=get_moisture_hex()
time.sleep(0.4)
ec_final_return=get_ec_hex()
time.sleep(0.4)
ph_final_return=get_ph_hex()
time.sleep(0.4)
nitro_final_return=get_nitro_hex()
time.sleep(0.4)
phos_final_return=get_phos_hex()
time.sleep(0.4)
pot_final_return=get_pot_hex()
time.sleep(0.4)

temp_final_string=f"AT+send=\"TEMPERATURE--->{temp_final_return}\""
moisture_final_string=f"AT+send=\"Humidity--->{moisture_final_return}\""
ec_final_string=f"AT+send=\"Conductivity--->{ec_final_return}\""
ph_final_string=f"AT+send=\"PH--->{ph_final_return}\""
nitro_final_string=f"AT+send=\"Nirogen--->{nitro_final_return}\""
phos_final_string=f"AT+send=\"Phosphorus--->{phos_final_return}\""
pot_final_string=f"AT+send=\"Potassium--->{pot_final_return}\""

temp_command=temp_final_string
moisture_command=moisture_final_string
ec_command=ec_final_string
ph_command=ph_final_string
nitro_command=nitro_final_string
phos_command=phos_final_string
pot_command=pot_final_string

join_func()
time.sleep(0.2)
send_temp_func(temp_command)
time.sleep(0.2)
send_humidity_func(moisture_command)
time.sleep(0.2)
send_ec_func(ec_command)
time.sleep(0.2)
send_ph_func(ph_command)
time.sleep(0.2)
send_nitro_func(nitro_command)
time.sleep(0.2)
send_phos_func(phos_command)
time.sleep(0.2)
send_pot_func(pot_command)

while 1:
 utility_func()
 time.sleep(10)

ser1.close()
