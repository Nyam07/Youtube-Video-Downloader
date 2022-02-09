
from optparse import Values
from tkinter.ttk import Combobox
import tkinter as tk
from tkinter import *
from pytube import YouTube
from tkinter import filedialog, messagebox

def createwidgets():
    link_label = Label(root, text="Youtube Url:", bg="#FFE4C4",
                       height=2, relief=GROOVE, font=("Times New Roman", 11, "bold"))
    link_label.place(x=50, y=10)

    root.link_text = Entry(root, width=60, textvariable=video_link, font=(
        "Times New Roman", 11, "bold"), relief=RIDGE)
    root.link_text.place(x=200, y=10, height=40)

    resolution_label = Label(root, text="Resolution:",
                             bg="#FFE4C4", font=("Times New Roman", 11, "bold"), height=2, relief=GROOVE)
    resolution_label.place(x=50, y=70)

    all_resolutions = ('1080p', '720p', '480p', '360p', '240p')
    root.resolution = Combobox(root, width=60, values=all_resolutions, font=(
        "Times New Roman", 11, "bold"), height=3)
    root.resolution.place(x=200, y=70, height=40)

    destination_label = Label(
        root, text="Destination:", bg="#FFE4C4", height=2, font=("Times New Roman", 11, "bold"), relief=GROOVE)
    destination_label.place(x=50, y=130)

    root.destination_text = Entry(
        root, width=45, textvariable=download_path, font=("Times New Roman", 11, "bold"), relief=RIDGE)
    root.destination_text.place(x=200, y=130, height=40)

    browse_btn = Button(root, text="Browse:", command=browse,
                        width=10, bg="#05E8E0", font=("Times New Roman", 12, "bold"), relief=RAISED)
    browse_btn.place(x=600, y=125, height=50)

    download_btn = Button(root, text="Download Video", width=30,
                          height=3, command=download, bg="#FF0000", fg="white", font=("Times New Roman", 18, "bold"), relief=RAISED)
    download_btn.place(x=200, y=220)


# code for the browse button
def browse():
    # initialize the directory to save the file
    download_dir = filedialog.askdirectory(initialdir="Your Directory Path")
    # set the initialized folder as the selected location
    download_path.set(download_dir)

def get_resolutions(highest_resolution):
    pass

def download():
    url = video_link.get()
    folder = download_path.get()

    get_video = YouTube(url)
    highest_resolution = get_video.streams.get_highest_resolution().resolution
    get_video = get_video.streams.get_by_resolution('360p')
    get_video.download(folder)

    messagebox.showinfo("Success!!", "Downloaded successfully. You will find your video at \n" + folder)

root = tk.Tk()
root.geometry("940x470")
root.resizable(False, False)
root.title("Youtube Download")
root.config(background="#000000")

video_link= StringVar()
download_path = StringVar()

createwidgets()



root. mainloop()
