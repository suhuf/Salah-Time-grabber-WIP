import requests
import json
import customtkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

root = customtkinter.CTk()

root.geometry("500x350")

def login():
    print("Test")

frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)

label = customtkinter.CTkLabel(master=frame, text="Login System", font=("Roboto", 24))

label.pack(pady=12, padx=10)

entry1 = customtkinter.CTkEntry(master=frame, placeholder_text="???")

entry1.pack(pady=12, padx=10)

entry2 = customtkinter.CTkEntry(master=frame, placeholder_text="?????", show="*")
entry2.pack(pady=12, padx=10)

button = customtkinter.CTkButton(master=frame, text="Login", command=login)

button.pack(pady=12, padx=10)

root.mainloop()






url = 'http://www.islamicfinder.us/index.php/api/prayer_times'

z = input("Enter a zipcode ")

c = input("Enter a Country ")

if c == "USA" or "UnitedStates" or "America":
    c = "US"



ip = {'user_ip': '73.133.80.20'}

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



