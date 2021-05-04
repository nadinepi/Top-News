import tkinter
import requests

from tkinter import *
import webbrowser
from PIL import ImageTk, Image


def callback(url):
    webbrowser.open_new(url)


root = tkinter.Tk()

root.title('Top News')
root.geometry('1200x900')

l1 = tkinter.Label(root, text='Enter a news source:', font='helvetica 15', justify=tkinter.RIGHT)
l1.grid(row=1, column=0)

source = tkinter.StringVar()
source.set('bbc-news')
e1 = tkinter.Entry(root, textvariable=source)
e1.grid(row=1, column=1)

infodisplay = tkinter.StringVar()
infodisplay2 = tkinter.StringVar()
infodisplay3 = tkinter.StringVar()
infodisplay4 = tkinter.StringVar()
infodisplay5 = tkinter.StringVar()

infodisplay.set("Most recent news will appear here!")


def getnews():
    global infodisplay
    global infodisplay2
    global infodisplay3
    global infodisplay4
    global infodisplay5

    global link
    global link2
    global link3
    global link4
    global link5

    s = (source.get())

    url = ('https://newsapi.org/v2/top-headlines?sources=' + s + '&apiKey=481c639b11c3489cb44f3bc0286d6247')
    json = requests.get(url).json()
    news = "News #1 provided by" + " " + s
    author = json['articles'][0]['author']
    d = json['articles'][0]['description']
    link = json['articles'][0]['url']

    information = news + "\nAuthor: " + author + "\nDescription: " + d + "\nLink to the full article: " + link
    infodisplay.set(information)

    news2 = "News #2 provided by" + " " + s
    author2 = json['articles'][1]['author']
    d2 = json['articles'][1]['description']
    link2 = json['articles'][1]['url']
    info2 = "\n" + news2 + "\nAuthor: " + author2 + "\nDescription: " + d2 + "\nLink to the full article: " + link2
    infodisplay2.set(info2)

    news3 = "News #3 provided by" + " " + s
    author3 = json['articles'][2]['author']
    d3 = json['articles'][2]['description']
    link3 = json['articles'][2]['url']
    info3 = "\n" + news3 + "\nAuthor: " + author3 + "\nDescription: " + d3 + "\nLink to the full article: " + link3
    infodisplay3.set(info3)

    news4 = "News #4 provided by" + " " + s
    author4 = json['articles'][3]['author']
    d4 = json['articles'][3]['description']
    link4 = json['articles'][3]['url']
    info4 = "\n" + news4 + "\nAuthor: " + author4 + "\nDescription: " + d4 + "\nLink to the full article: " + link4
    infodisplay4.set(info4)

    news5 = "News #5 provided by" + " " + s
    author5 = json['articles'][4]['author']
    d5 = json['articles'][4]['description']
    link5 = json['articles'][4]['url']
    info5 = "\n" + news5 + "\nAuthor: " + author5 + "\nDescription: " + d5 + "\nLink to the full article: " + link5
    infodisplay5.set(info5)


b1 = tkinter.Button(root, text='Get News', command=getnews)
b1.grid(row=1, column=2)

options = tkinter.Label(root,
                        text="\nChoose from the following:\n\n"
                             "- bbc-news\n"
                             "- abc-news\n"
                             "- mashable\n"
                             "- buzzfeed\n"
                             "- business-insider\n"
                             "- cbc-news\n"
                             "- msnbc\n"
                             "- rt\n"
                             "- the-wall-street-journal\n"
                             "- vice-news\n"
                             "- wired\n"
                             "- time. \n\nPlease type the news sources exactly as shown!",
                        wraplength=200, justify=tkinter.LEFT, font='helvetica 14', padx=30)
options.grid(row=3, column=0)

label = tkinter.Label(root, text="TOP NEWS", font='helvetica 30 bold', pady=10, fg='dodgerblue')
label.grid(row=0, column=0, padx=(70,0))

l2 = tkinter.Label(root, textvariable=infodisplay, wraplength=550, pady=30, padx=30, font='helvetica 14', borderwidth=2,
                   relief="solid", cursor='hand')
l2.grid(row=3, column=3)
l2.bind("<Button-1>", lambda e: callback(link))

l3 = tkinter.Label(root, textvariable=infodisplay2, wraplength=550, font='helvetica 14', cursor='hand')
l3.grid(row=4, column=3)
l3.bind("<Button-1>", lambda e: callback(link2))

l4 = tkinter.Label(root, textvariable=infodisplay3, wraplength=550, font='helvetica 14', cursor='hand')
l4.grid(row=5, column=3)
l4.bind("<Button-1>", lambda e: callback(link3))

l5 = tkinter.Label(root, textvariable=infodisplay4, wraplength=550, font='helvetica 14', cursor='hand')
l5.grid(row=6, column=3)
l5.bind("<Button-1>", lambda e: callback(link4))

l6 = tkinter.Label(root, textvariable=infodisplay5, wraplength=550, font='helvetica 14', cursor='hand')
l6.grid(row=7, column=3)
l6.bind("<Button-1>", lambda e: callback(link5))

img = ImageTk.PhotoImage(Image.open('top news logo.png').resize((50, 50)))

#The Label widget is a standard Tkinter widget used to display a text or image on the screen.
panel = tkinter.Label(root, image=img)
panel.image = img
#The Pack geometry manager packs widgets in rows or columns.
panel.grid(row=0, column=0, sticky='w', pady=30, padx=15)


root.mainloop()
