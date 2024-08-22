# Task 3 : WEATHER APPLICATION
#%%
# %%
from tkinter import *
from tkinter import ttk
import requests    # for sending a http request to web service and retrieve data from api
from PIL import Image, ImageTk  #  for inserting an image and ImageTk used to convert image into that format which displayed tkinter GUI element

def auto_get_location():
    # Get IP-based location using ipinfo.io
    location_data = requests.get("https://ipinfo.io").json()
    location = location_data['city']  # Extract city name
    city_name.set(location)
    data_get()


def data_get():
    city = city_name.get()
    data =requests.get("https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=daa9c2c6d17f8f008933b1b4b5b13a7f").json() # retreiving the data from api and convert that data in json format
    # after response, extracting the relavant data from that data
    wc_label_1.config(text=data["weather"][0]["main"])
    wd_label_2.config(text=data["weather"][0]["description"])
    wt_label_3.config(text=str(round(data["main"]["temp"] - 273.15, 2))+"°C")
    per_label_4.config(text=str(data["main"]["pressure"])+"hPa")

win = Tk()
win.title("Weather App")
win.config(bg="dodger blue")  # Light Cyan
win.geometry("550x650")

# inserting the logo image
logo_img = Image.open("/home/shivam/Pictures/Screenshots/weather_app.png") # opening an image file
logo_img = logo_img.resize((100, 100), Image.BICUBIC) # adjusting size of image
logo = ImageTk.PhotoImage(logo_img) # ImageTk used to convert image into that format which displayed tkinter GUI element
logo_label = Label(win, image=logo, bg="yellow") 
logo_label.place(x=225, y=20)


# title of app
name_label = Label(win, text="Weather App",font=("Helvetica",36,"bold"), foreground="darkblue",background="dodger blue")
name_label.place(x=120, y=140, height=50, width=310)

# drop_down list for city names
city_name = StringVar()
list_name = ["Andhra Pradesh", "Arunachal Pradesh", "Assam", "Bihar", "Chhattisgarh", "Goa", "Gujarat", "Haryana", "Himachal Pradesh", "Jammu and Kashmir", "Jharkhand", "Karnataka", "Kerala", "Madhya Pradesh",  "Maharashtra", "Manipur", "Meghalaya", "Mizoram", "Nagaland", "Odisha", "Punjab", "Rajastha", "Sikkim", "Tamil Nadu", "Telangana", "Tripura", "Uttar Pradesh", "Uttarakhand", "West Bengal"]



com = ttk.Combobox(win, values=list_name,font=("Helvetica",18),textvariable=city_name)
com.place(x=100, y=220, height=40, width=350)



# details of weather
wc_label = Label(win, text="Weather Condition",font=("Helvetica",16),foreground="black", background="dodger blue")
wc_label.place(x=40, y=300, height=40, width=200)
wc_label_1 = Label(win, text="", font=("Helvetica",16,"bold"),foreground="darkblue", background="dodger blue")
wc_label_1.place(x=300, y=300, height=40, width=200)

wd_label = Label(win, text="Description", font=("Helvetica",16),foreground="black", background="dodger blue")
wd_label.place(x=40, y=370, height=40, width=200)
wd_label_2 = Label(win, text="", font=("Helvetica",16,"bold"),foreground="darkblue", background="dodger blue")
wd_label_2.place(x=300, y=370, height=40, width=200)



wt_label = Label(win, text="Temperature", font=("Helvetica", 16),foreground="black", background="dodger blue")
wt_label.place(x=40, y=440, height=40, width=200)
wt_label_3 = Label(win, text="", font=("Helvetica", 16, "bold"),foreground="darkblue", background="dodger blue")
wt_label_3.place(x=300, y=440, height=40, width=200)



per_label = Label(win, text="Pressure", font=("Helvetica", 16),foreground="black", background="dodger blue")
per_label.place(x=40, y=510, height=40, width=200)
per_label_4 = Label(win, text="", font=("Helvetica", 16, "bold"),foreground="darkblue", background="dodger blue")
per_label_4.place(x=300, y=510, height=40, width=200)



# submit_button
button_do = Button(win, text="Get Weather", font=("Helvetica", 14, "bold"),background="deep sky blue", foreground="white", command=data_get)
button_do.place(y=580, height=50, width=200, x=50)

# auto detect location button
button_auto = Button(win, text="Auto Detect Location", font=("Helvetica", 14, "bold"),background="deep sky blue", foreground="white", command=auto_get_location)
button_auto.place(y=580, height=50, width=200, x=300)

win.mainloop()
