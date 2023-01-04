from ast import Bytes

import tkinter as tk
from tkinter import *

from pytube import YouTube
from tkinter import filedialog , messagebox
from PIL import ImageTk, Image
import urllib.request, io
global location


class Ytube:
    
   
    def __init__(self) :
        self.a = None
        
        # video_link = StringVar()
        # location = StringVar()
        # self.url = url
        # print(self.url)
        # self.url = "https://www.youtube.com/watch?v=A66TYFdz8YA"
        # self.folder = location.get()


    def download(self,a,path,url):  
        if path == "":
            path = "C://Users//"  
        print(path)
        try:
            get_video = YouTube(url)

        except :
            messagebox.showinfo("Error",f'Video url {url} is unavaialable, skipping.')
            print(f'Video {url} is unavaialable, skipping.')
        else:
            
                if a == "hight":
                    print("hight")
                    get_stream = get_video.streams.get_highest_resolution()
                    print(get_video.title)

                    get_stream.download(path)
                    messagebox.showinfo("Success!!", "Download Successful! you will find your video at \n" + path)
                
                elif a == "low":
                    print("low")
                    get_stream = get_video.streams.get_lowest_resolution()
                    get_stream.download(path)
                    
                    messagebox.showinfo("Success!!", "Download Successful! you will find your video at \n" + path)
                
                elif a == "audio":
                    print("audio")
                    print(url)
                    get_stream = get_video.streams.get_audio_only()
                    get_stream.download(path)
                    messagebox.showinfo("Success!!", "Download Successful! you will find your video at \n" + path)



                elif a  == "chack":
                    try:
                        host='http://google.com'
                        urllib.request.urlopen(host) #Python 3.x
                        
                    except:
                            messagebox.showinfo("Error","no internet!" )

                    else:   
                        imgurl=urllib.request.urlopen(get_video.thumbnail_url).read()  
            
                        img = ImageTk.PhotoImage(Image.open(io.BytesIO(imgurl)).resize((200, 170)))

                        label = Label(root,width=200,height=170,image=img,bg="#ffffff")
                        label.place(x=200,y=200)
                        label = Label(root,text=get_video.title,bg="#ff00ff")
                        label.place(x=10,y=400)
                        c = Canvas(root, width=400, height=400)
                        c.create_image(0,0, anchor='nw', image=img,bgcolor="#ffffff")

                        c.place(x=200,y=200)
                        
                    

        
            
            

    
               
    
    def browse(self ):
        download_dir = filedialog.askdirectory(initialdir="Your  location to download")

        location.set(download_dir)

    



        
            



        

class Gui:
    global q
    
    

    def __init__(self,root) :
        root.geometry("620x545")
        root.resizable(False,False)
        root.title("Youtube Downloder")
        root.config(background="#f1effd")
        self.q = Ytube()
    
    

    def hight(self):
        x = "hight"
        
        path = location.get()
        url = video_link.get()
        self.q.download(x,path,url)
        
        
    def low(self):
        x = "low"
        path = location.get()
        url = video_link.get()
        self.q.download(x,path,url)
        
    def audio(self):
        x = "audio"
        path = location.get()
        url = video_link.get()
        self.q.download(x,path,url)

    def chack(self):
        x = "chack"
        path = location.get()
        url = video_link.get()
        self.q.download(x,path,url)
        
    
        
        


    def creatWidgets(self,video_link,location):

        link_label = Label(root, text="YouTube Url: ", bg="#E8D579")
        link_label.grid(row=0, column=0 ,pady=5, padx=5)
        
        root.link_text = Entry(root,width=60 ,textvariable = video_link)
        root.link_text.grid(row=0,column=1,padx=5,pady=5)

        chooseLoc = Label(root, text="Destination: ", bg="#E8D579")
        chooseLoc.grid(row=1, column=0 ,pady=5, padx=5)

        root.destination = Entry(root,width=60 ,textvariable = location)
        root.destination.grid(row=1,column=1,padx=5,pady=5)

        check_but = Button(root, text="Search", command=self.chack, width=10, bg="#5EFBFF")
        check_but.grid(row=0,column=2,padx=5,pady=5)

        browse_but = Button(root, text="Browse", command=self.q.browse, width=10, bg="#5EFBFF")
        browse_but.grid(row=1,column=2,padx=5,pady=5)

        download_but = Button(root, text='''Highest Resolution''', command=self.hight, width=15, bg="#5EFBFF")
        download_but.grid(row=2,column=0,padx=4,pady=5)

        download_but = Button(root, text='''Lowest Resolution''', command=self.low, width=15, bg="#5EFBFF")
        download_but.grid(row=2,column=1,padx=0,pady=0)

        download_but = Button(root, text=" Audio", command=self.audio, width=15, bg="#5EFBFF")
        download_but.grid(row=2,column=2,padx=4,pady=5)

        link_label = Label(root, text="Developed By Tushant Parjapat", bg="#E8D579")
        link_label.grid(row=3, column=1 ,pady=5, padx=5)
        

        
    
    # l = Label(farme,text="imageasdfasdfasdfasdfasdfasdfdfa  fasdfasdfasdf=img",foreground="red" ,width=50,height=10 ) farme.grid()
   

 

   
   

root = tk.Tk()

video_link = StringVar()

location = StringVar()

def creat(self,):
        gui_obj = Gui()
        return gui_obj.creatWidgets(video_link,location)



gui_obj = Gui(root)
gui_obj.creatWidgets(video_link,location)

# root.iconbitmap(r'favicon.ico')















root.mainloop()