import requests, random
from bs4 import BeautifulSoup
from tkinter import *
def pick_random_actor():
    num=random.randint(1,1000)
    zeroes=7-len(str(num))
    retrieve_actor_data(("0"*zeroes)+str(num))
def retrieve_actor_data(actor_num):
    info_URL="https://www.imdb.com/name/nm"+actor_num+"/"
    movie_URL = "https://www.imdb.com/filmosearch/?sort=num_votes&explore=title_type&role=nm"+actor_num+"&ref_=nm_flmg_shw_4"
    page = requests.get(info_URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    name = soup.find_all('span', class_='itemprop')
    name=str(name[0].text.strip())
    age=soup.find(id="name-born-info")
    age=str(age.text.strip().replace("\n","").replace("      "," ").replace("  "," ")).replace(":",": ")
    page = requests.get(movie_URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    movies=soup.find_all("h3", class_="lister-item-header")
    movie_1=movies[0].text.strip().replace("\n"," ")
    movie_2=movies[1].text.strip().replace("\n"," ")
    movie_3=movies[2].text.strip().replace("\n"," ")
    data=name+"\n"+age+"\n"+movie_1+"\n"+movie_2+"\n"+movie_3
    info_label.configure(text=data)
window=Tk()
window.geometry("650x300")
the_canvas = Canvas(window,width=651,height=501, highlightthickness=0,bg="#2a75d5")
the_canvas.create_rectangle(0,220,650,300,fill="#5590DD",outline="")
the_canvas.create_rectangle(0,250,650,270,fill="#832cd3",outline="")
the_canvas.create_rectangle(0,0,651,65,fill="#5590DD",outline="")
the_canvas.create_rectangle(0,0,651,55,fill="#832cd3",outline="")
the_canvas.create_rectangle(0,0,530,45,fill="#5590DD",outline="")
the_canvas.create_oval(510,0,550,44,fill="#5590DD",outline="")
the_canvas.place(x=-1,y=-1)
window.title("Random IMDB Profile Generator")
window.resizable(False, False)
start_label=Label(text="  Random IMDB Profile Generator ",font=("fixedsys",20),bg="#5590DD",fg="white")
start_label.pack(side=LEFT, anchor=N)
info_label=Label(text="Use this program to learn about people involved in movies and television! Press the button to show a new profile and three productions they were involved with!",font=("fixedsys",15),fg="white",bg="#2a75d5",wraplength=550,justify=LEFT)
info_label.place(x=50,y=75)
the_button=Button(text="NEW PROFILE",font=("fixedsys",20),borderwidth= 5,bg="#2a75d5",fg="white",command=pick_random_actor)
the_button.place(x=50,y=230)
window.mainloop()
