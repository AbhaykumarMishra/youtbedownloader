
# youtbe video downloader 

import tkinter as tk 
from tkinter import Variable, ttk , messagebox, filedialog
import os 
from pytube import YouTube

#main function 
def action():

    url = url_entry.get()
    video_formate = video_var.get()

    try:
        if video_formate == 'mp3':
            youtube = YouTube(url)
            audio = youtube.streams.filter(only_audio=True).first()
            audio.download('/home/abhay/Downloads/youtube/audio')
        else:
            youtube = YouTube(url)
            video = youtube.streams.filter(res=str(video_formate)).first()
            video.download('/home/abhay/Downloads/youtube/video')


    except:
        messagebox.showwarning(title='warning!',message="url can't we blank ")


# create maine window 
win = tk.Tk() 
win.title('Youtube_Donloade')
win.geometry('640x430')


# creating lable to sow youtbe Downloader 
aap_name = tk.Label(win,text='YouTube Downloader : ',fg='red',font=('Arial',15,'bold'))
aap_name.pack(side=tk.TOP,fill=tk.X)

# from where i am creating url entry box and combobox to selt video formate 
urls_label = tk.Label(win,text='Enter Your Youtube urls : ',font=('Arial',14,'bold'))
urls_label.pack()

lable1= tk.Frame(win)
lable1.pack()

entry_var = tk.StringVar()
url_entry=tk.Entry(lable1,width=50,textvariable=entry_var)
url_entry.select_range(0,tk.END)
url_entry.pack(side=tk.LEFT,padx=5)
url_entry.focus()

video_var = tk.StringVar()
select_video = ttk.Combobox(lable1,width=14,state='readonly',textvariable=video_var)
select_video['values']=('720p','480p','360p','mp3')
select_video.current(1)
select_video.pack(side=tk.RIGHT,padx=5)

# creating Donload button 
Download = tk.Button(win ,text = 'Download',command=action)
Download.pack(pady=5)




win.mainloop()