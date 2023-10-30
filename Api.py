import requests
import json

url = 'http://www.islamicfinder.us/index.php/api/prayer_times'

z = input("Enter a zipcode ")

c = input("Enter a Country ")

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
        dict_keys[j] = i.replace("%", " ")

t_fajr = str(dict_keys[0])
t_dhur = str(dict_keys[1])
t_asr = str(dict_keys[2])
t_maghrib = str(dict_keys[3])
t_isha = str(dict_keys[4])

print("Fajr Time: " + t_fajr)
print("Dhur Time: " + t_dhur)
print("Asr Time: " + t_asr)
print("Maghrib Time: " + t_maghrib)
print("Isha Time: " + t_isha)

#print(json.dumps(a_dict, indent=4))



