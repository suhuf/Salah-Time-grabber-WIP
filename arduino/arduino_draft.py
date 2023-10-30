import requests
import json
import serial
from time import sleep

# Serial Object

t = 0 



arduino = serial.Serial('COM6', 9600) # Change 'COM6' according to the port on your arduino

url = 'http://www.islamicfinder.us/index.php/api/prayer_times'

z = 20874

c = "US"

if c == "USA" or "UnitedStates" or "America":
    c = "US"





a = requests.post(url, data={'zipcode': z, 'country': c })

print("        ")

print("Response Code: " + str(a.status_code))

print("        ")
api_data = a.json()


a_dict = a.json()
    
f_key = str(api_data['results']['Fajr'])
d_key = str(api_data['results']['Dhuhr'])
a_key = str(api_data['results']['Asr'])
m_key = str(api_data['results']['Maghrib'])
i_key = str(api_data['results']['Isha'])

dict_keys = [f_key, d_key, a_key, m_key, i_key]

for j,i in enumerate(dict_keys):
    if "%" in i:
        dict_keys[j] = i.replace("%", "")

t_fajr = str(dict_keys[0])
t_dhur = str(dict_keys[1])
t_asr = str(dict_keys[2])
t_maghrib = str(dict_keys[3])
t_isha = str(dict_keys[4])

St_fajr = str(dict_keys[0]) + " fend"
St_dhur = str(dict_keys[1]) + " dend"
St_asr = str(dict_keys[2]) + " aend"
St_maghrib = str(dict_keys[3]) + " mend"
St_isha = str(dict_keys[4]) + " iend"

print("Fajr Time: " + t_fajr)
print("Dhur Time: " + t_dhur)
print("Asr Time: " + t_asr)
print("Maghrib Time: " + t_maghrib)
print("Isha Time: " + t_isha)

    #print(json.dumps(a_dict, indent=4))

serial_list = [St_fajr, St_dhur, St_asr, St_maghrib, St_isha]

serial_str = ", ".join(serial_list[0:5])
print(serial_str)

# While loop was removed for debugging, Ideally this will contain a While loop
arduino.write(serial_str.encode())

sleep(5)

print("New data written")

print("port closed")
