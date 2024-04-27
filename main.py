import requests
from tkinter import *
import key_api as ka # importing a module with a key

root = Tk()


def get_weather():
    #getting weather data
    city = cityfield.get()
    key = ka.key #you can write your own key. For example"key = 103249b37d33b25r1y48827c734gf15cd"
    res = requests.get('https://api.openweathermap.org/data/2.5/weather',
                       params={'q': city, 'units': 'metric', 'lang': 'en', 'appid': key})
    data = res.json()

    temp = str(data['main']['temp'])
    temp_min = str(data['main']['temp_min'])
    temp_max = str(data['main']['temp_max'])

    info[
        'text'] = f"{str(data['name'])}:\nCurrent temperature: {temp}\nMinimum temperature: {temp_min}\nMaximum temperature: {temp_max}"


'''making a graphical widget interface'''

root['bg'] = 'gray99'
root.title('Your weather')
root.geometry('500x400')

frame_top = Frame(root, bg='#778899')
frame_top.place(relwidth=1, relheight=1)
frame_lower = Frame(root, bg='white')
frame_lower.place(relx=0.15, rely=0.3, relwidth=0.7, relheight=0.4)

cityfield = Entry(frame_top, bg='white', font=15)
cityfield.pack()

btn = Button(frame_top, text='SHOW THE WEATHER', command=get_weather)
btn.pack()

info = Label(frame_lower, text='⭡ Where can I show the weather? ⭡', bg='white', font=25)
info.pack()

root.mainloop()

root.mainloop()
