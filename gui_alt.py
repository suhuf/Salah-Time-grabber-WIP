import requests
import json

import tkinter as tk

from tkinter import messagebox

from tkinter import simpledialog

url = 'http://www.islamicfinder.us/index.php/api/prayer_times'

class Gui:
    def __init__(self):

        self.root = tk.Tk()

        self.label = tk.Label(self.root, text="Message", font=('Arial'))

        self.label.pack(padx=10, pady=10)

        self.textbox = tk.Text(self.root, height=5, font=('Arial', 16))

        self.textbox.bind("<KeyPress>", self.sc)

        self.textbox.pack(padx=10, pady=10)

        self.button = tk.Button(self.root, text="Send", font=('Arial', 18), command=self.api_call)

        self.button.pack(padx=10, pady=10)

        self.root.mainloop()

    def api_call(self):

    
        global entry
        z = 20874
        c = 'US'

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

        """ print("Fajr Time: " + t_fajr)
        print("Dhur Time: " + t_dhur)
        print("Asr Time: " + t_asr)
        print("Maghrib Time: " + t_maghrib)
        print("Isha Time: " + t_isha) """

        messagebox.showinfo(title="Message", message="Response Code: " + str(a.status_code) + " Fajr Time: " + str(t_fajr)
        + "Dhur Time: " + str(t_dhur)
        + "Asr Time: " + str(t_asr)
        + "Maghrib Time: " + str(t_maghrib) +
        "Isha Time: " + str(t_isha) )
        
        pass

    def sc(self, event):
        
        pass

Gui()
