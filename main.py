"""
main.py is the main file of project
To start the project run this file

REQUIRED ---
1. pip install easygui
2. pip install requests
3. pip install tkinter
4. pip install mplcursors
"""

import sys
import easygui
from matplotlib import use
import requests
import tkinter as tk
import json
import urllib.request
from PIL import Image
import compare
import numpy as np
import mplcursors

from csv import writer
import pandas as pd
import os
import matplotlib.pyplot as plt
from pandas.core import series
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,NavigationToolbar2Tk)

profile = open("settings.st","r+")
username = profile.read() #username will be NONE if user is not logged in
profile.close()

"""
Function to logout
"""
def logout():
    profile = open("settings.st","w+")
    profile.write("NONE")
    profile.close()
    sys.exit()

def showGraph():
    df = pd.read_csv('cf_data.csv')
    df.dropna(inplace=True)
    df.plot()
    plt.title("Rating change")
    plt.show()

def performance():
    df=pd.read_csv('user_data.csv')
    df.dropna(inplace=True)
    df = df[df['Username'].str.contains(username)]
    print(df)
    tempz=["AC","WA","TLE"]
    imp=df.index[0]
    x=df.at[imp,"AC"]
    y=df.at[imp,"WA"]
    z=df.at[imp,"TLE"]
    sizes = [x,y,z]
    temp=np.array([x,y,z])
    print(temp)
    colors = ['#41ab0c','#d9442e','#2376eb']
    fig1, ax1 = plt.subplots()
    ax1.axis('equal')  
    plt.tight_layout()
    def autopct_format(values):
        def my_format(pct):
            total = sum(values)
            val = int(round(pct*total/100.0))
            return '{v:d}'.format(v=val)
        return my_format
    ax1.pie(sizes, labels = tempz, autopct = autopct_format(sizes), colors=colors)
    plt.show()

def num_stats():
    df=pd.read_csv('user_data.csv')
    df.dropna(inplace=True)
    df = df[df['Username'].str.contains(username)]
    print(df)

    tempz1=["800","1000","1200","1400","1600","1800"]
    imp=df.index[0]
    x1=df.at[imp,"800"]
    x2=df.at[imp,"1000"]
    x3=df.at[imp,"1200"]
    x4=df.at[imp,"1400"]
    x5=df.at[imp,"1600"]
    x6=df.at[imp,"1800"]
    x=np.array(tempz1)
    tempz2=[x1,x2,x3,x4,x5,x6]
    print(tempz2)
    y=np.array(tempz2)
    plt.bar(x,y,color="hotpink")
    cursor = mplcursors.cursor(hover=mplcursors.HoverMode.Transient)
    @cursor.connect("add")
    def on_add(sel):
        x, y, width, height = sel.artist[sel.index].get_bbox().bounds
        sel.annotation.set(text=f"{int(height)}", position=(0, 20), anncoords="offset points")
        sel.annotation.xy = (x + width / 2, y + height)
    plt.xlabel("Difficulty Level")
    plt.ylabel("Number of questions") 
    plt.show()

"""
Function to get details of user logged in
"""

def GUI(response):
    window = tk.Tk()

    width= window.winfo_screenwidth() 
    height= window.winfo_screenheight()

    window.geometry("%dx%d" % (width, height))

    window.title("Codeforces User Data Analysis")

    menubar = tk.Menu(window)
    file = tk.Menu(menubar,tearoff=0)
    menubar.add_cascade(label='File',menu=file)

    file.add_command(label='Show Graph',command=showGraph)
    file.add_command(label='Log Out',command=logout)

    window.config(background='#ffffff',menu=menubar)

    tmp = json.loads(response)
    rank = tmp['result'][0]['rank']

    #Get the standings of tags

    label = tk.Label(window,text="\n",fg='#000000',bg='#ffffff',font=20)
    label.pack()

    label = tk.Label(window,text="Codeforces User Data Analysis",fg='#000000',bg='#ffffff',font="Vardana 24 underline")
    label.pack()

    tmp_text = tmp['result'][0]['firstName']+" "+tmp['result'][0]['lastName']

    try:
        tk.Label(window,text = "Username: ",font=14,bg='#ffffff').place(x = 500,y = 160) #40
        if(rank=='pupil'):
            label = tk.Label(window,text=username,fg='#008000',bg='#ffffff',font=20).place(x = 650,y = 160)
            label.pack()
        elif(rank=='newbie'):
            label = tk.Label(window,text=username,fg='#808080',bg='#ffffff',font=20).place(x = 650,y = 160)
            label.pack()
        elif(rank=='specialist'):
            label = tk.Label(window,text=username,fg='#03a89e',bg='#ffffff',font=20).place(x = 650,y = 160)
            label.pack()
        elif(rank=='expert'):
            label = tk.Label(window,text=username,fg='#0000ff',bg='#ffffff',font=20).place(x = 650,y = 160)
            label.pack()
        elif(rank=='master'):
            label = tk.Label(window,text=username,fg='#ff8c00',bg='#ffffff',font=20).place(x = 650,y = 160)
            label.pack()
        elif(rank=='candidate master'):
            label = tk.Label(window,text=username,fg='#a0a',bg='#ffffff',font=20).place(x = 650,y = 160)
            label.pack()
        elif(rank=='international master'):
            label = tk.Label(window,text=username,fg='#ff8c00',bg='#ffffff',font=20).place(x = 650,y = 160)
            label.pack()
        elif(rank=='grandmaster'):
            label = tk.Label(window,text=username,fg='#ff0000',bg='#ffffff',font=20).place(x = 650,y = 160)
            label.pack()
        elif(rank=='legendary grandmaster'):
            label = tk.Label(window,text=username,fg='#ff0000',bg='#ffffff',font=20).place(x = 650,y = 160)
            label.pack()
    except:
        """"""
    
    try:
        tk.Label(window,text = "Name: ",font=14,bg='#ffffff').place(x = 500,y = 230)
        tk.Label(window,text = tmp_text,font=14,bg='#ffffff').place(x = 650,y = 230)
    except:
        """"""
    
    try:
        tk.Label(window,text = "Country: ",font=14,bg='#ffffff').place(x = 500,y = 300)
        tk.Label(window,text = tmp['result'][0]['country'],font=14,bg='#ffffff').place(x = 650,y = 300)
    except:
        """"""
    
    try:
        tk.Label(window,text = "City: ",font=14,bg='#ffffff').place(x = 500,y = 370)
        tk.Label(window,text = tmp['result'][0]['city'],font=14,bg='#ffffff').place(x = 650,y = 370)
    except:
        """"""
    
    try:
        tk.Label(window,text = "Rating: ",font=14,bg='#ffffff').place(x = 500,y = 440)
        tk.Label(window,text = tmp['result'][0]['rating'],font=14,bg='#ffffff').place(x = 650,y = 440)
    except:
        """"""

    try:
        tk.Label(window,text = "Contribution: ",font=14,bg='#ffffff').place(x = 500,y = 510)
        tk.Label(window,text = tmp['result'][0]['contribution'],font=14,bg='#ffffff').place(x = 650,y = 510)
    except:
        """"""

    try:
        all_contests_given = requests.get('https://codeforces.com/api/user.rating?handle='+username)
        json_all_contests_given = json.loads(all_contests_given.text)

        total_contests_given = len(json_all_contests_given['result'])
        cnt = 0
        csv_f = open("cf_data.csv",'w')
        writer_object=writer(csv_f,lineterminator='\n')
        writer_object.writerow(["Rating"])
        writer_object.writerow([json_all_contests_given['result'][0]['oldRating']])
        cnt = cnt + 1

        for i in range(cnt,total_contests_given+1):
            writer_object.writerow([json_all_contests_given['result'][i-1]['newRating']])
        
        csv_f.close()
        fig = Figure(figsize = (5, 5),dpi = 100)
        df = pd.read_csv('cf_data.csv')
        df.dropna(inplace=True)
        plot1 = fig.add_subplot(111)
        plot1.plot(df)
        canvas =  FigureCanvasTkAgg(fig,master = window)  
        canvas.draw()
        canvas.get_tk_widget().place(x=900, y = 100)
        canvas.pack()
        toolbar = NavigationToolbar2Tk(canvas,window)
        toolbar.update()
        canvas.get_tk_widget().pack()
    except:
        """"""

    # tk.Button(window, text ="Show rating graph", command = showGraph).place(x=10, y = 600)
    tk.Button(window, text ="Performance by Submissions", command =performance).place(x=500, y = 700)  #750
    tk.Button(window, text ="Performance By Problem Rating", command =num_stats).place(x=825, y = 700) #900
    tk.Button(window, text ="Compare Rating With", command = lambda: compare.compare(username)).place(x=1175, y = 700) #550

    """Now store the data of rating changes in CSV file"""
    all_contests_given = requests.get('https://codeforces.com/api/user.rating?handle='+username)
    json_all_contests_given = json.loads(all_contests_given.text)

    total_contests_given = len(json_all_contests_given['result'])
    cnt = 0
    csv_f = open("cf_data.csv",'w')
    writer_object=writer(csv_f,lineterminator='\n')
    writer_object.writerow(["Rating"])
    writer_object.writerow([json_all_contests_given['result'][0]['oldRating']])
    cnt = cnt + 1

    for i in range(cnt,total_contests_given+1):
        writer_object.writerow([json_all_contests_given['result'][i-1]['newRating']])
    
    csv_f.close()
    
    window.mainloop()

""""
END
"""

if(username == "NONE"):
    cf_username = easygui.enterbox("You are not logged in! Please enter your username to log in..","Codeforces Analysis")
    if(cf_username == ""):
        easygui.msgbox("Invalid Username..","Codeforces Analysis")
    else:
        response = requests.get('https://codeforces.com/api/user.info?handles='+cf_username)
        response_text = response.text
        profile_write = open("settings.st","w+")
        profile_write.write(cf_username)
        username = cf_username
        profile_write.close()
        GUI(response_text)
else:
    response = requests.get('https://codeforces.com/api/user.info?handles='+username)
    response_text = response.text
    GUI(response_text)