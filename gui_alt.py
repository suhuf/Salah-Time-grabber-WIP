import requests
import json

import tkinter as tk

from tkinter import messagebox
from tkinter import *

import tkinter.simpledialog as sd

url = 'http://www.islamicfinder.us/index.php/api/prayer_times'

def on_entry_click(event):
   if textbox.get() == "Enter your zipcode":
      textbox.delete(0, tk.END)
      textbox.configure(foreground="black")

def on_focus_out(event):
   if textbox.get() == "":
      textbox.insert(0, "Enter your zipcode")
      textbox.configure(foreground="gray")

def api_call():
   
    global entry

    textbox.get()

    z = textbox.get()
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
   
root = tk.Tk()

mystr = StringVar()
mystr.set('enter zippy')

label = tk.Label(root, text="Message", font=('Arial'))

label.pack(padx=10, pady=10)

textbox = Entry(root, width=50, font=('Arial', 16))

textbox.insert(0, "Enter your zipcode")

textbox.bind("<FocusIn>", on_entry_click)
textbox.bind("<FocusOut>", on_focus_out)

textbox.pack(padx=30, pady=30)

textbox.get

button = tk.Button(root, text="Send", font=('Arial', 18), command= api_call)

button.pack(padx=10, pady=10)

root.mainloop()
