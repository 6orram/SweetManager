# Starting--------------------------------------------------------------------------------------------------------------------------------

print(""" 
  --------------------------------------------------------------------
    ______                                                       
   /      \                                                      
  |  $$$$$$\  ______    ______    ______   ______   ______ ____  
  | $$___\$$ /      \  /      \  /      \ |      \ |      \    \ 
  | $$    \ |  $$$$$$\|  $$$$$$\|  $$$$$$\ \$$$$$$\| $$$$$$\$$$$\ 
  | $$$$$$$\| $$  | $$| $$   \$$| $$   \$$/      $$| $$ | $$ | $$
  | $$__/ $$| $$__/ $$| $$      | $$     |  $$$$$$$| $$ | $$ | $$
   \$$    $$ \$$    $$| $$      | $$      \$$    $$| $$ | $$ | $$
    \$$$$$$   \$$$$$$  \$$       \$$       \$$$$$$$ \$$  \$$  \$$

  ------------------------ Sweet Manager -----------------------------                                                                                                                                                                                        
""")
print("Don't forget to check My GitHub")
print("https://github.com/6orram")


# Importing Mosules and Librarys :  -------------------------------------------------------------------------------------------------------

from os import path
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *
from tkinter import filedialog
from pytube import YouTube
import pygame
from time import sleep
import os

# functions :  ----------------------------------------------------------------------------------------------------------------------------

# function to show an error message when the path is not selected
def patherror():
  messagebox.showerror('Sweet Manager', 'No Path Selected!')

# function to show an error message when the link is incorrect
def linkerror():
  messagebox.showerror('Sweet Manager', 'Link Error!')

# function to ask and get the path where the App save the video
def getpath():
    path = filedialog.askdirectory()
    path_output.config(text=path)

# function to download video with highest resolution
def DownloadHigh():
  try:
    get_link = link_input.get()
    user_path = path_output.cget("text")
    if user_path == "No Path Selected!" or user_path == "":
      patherror()
      return False
    status.insert(END,"downloading.. \n")
    main_window.title("Downloading...")
    YouTube(get_link).streams.get_highest_resolution().download(user_path)
    status.insert(END,"downloadind Successfuly \n")
    main_window.title('Sweet Manager v1.0')
  except:
    linkerror()
    status.insert(END,"downloading failed!! \n")
    main_window.title('Sweet Manager v1.0')

# function to download video with lowest resolution
def DownloadLow():
  try:
    get_link = link_input.get()
    user_path = path_output.cget("text")
    if user_path == "No Path Selected!" or user_path == "":
      patherror()
      return False
    status.insert(END,"downloading.. \n")
    main_window.title("Downloading...")
    YouTube(get_link).streams.get_lowest_resolution().download(user_path)
    status.insert(END,"downloadind Successfuly \n")
    main_window.title('Sweet Manager v1.0')
  except:
    linkerror()
    status.insert(END,"downloading failed!! \n")
    main_window.title('Sweet Manager v1.0')

# function to download video in .mp3 format
def DownloadAudio():
  try:
    get_link = link_input.get()
    user_path = path_output.cget("text")
    if user_path == "No Path Selected!" or user_path == "":
      patherror()
      return False
    status.insert(END,"downloading.. \n")
    main_window.title("Downloading...")
    mp4 = YouTube(get_link).streams.get_audio_only().download(user_path)
    base, ext = os.path.splitext(mp4)
    mp3 = base + '.mp3'
    os.rename(mp4, mp3)
    status.insert(END,"downloadind Successfuly \n")
    main_window.title('Sweet Manager v1.0')
  except:
    linkerror()
    status.insert(END,"downloading failed!! \n")
    main_window.title('Sweet Manager v1.0')

# function for open path in explorer
def OpenLocation():
  try:
    os.startfile(path_output.cget("text"))
  except:
    patherror()

# function to paly music when the program start
pygame.mixer.init()
def PlayMusic():
  pygame.mixer.music.load("file/sound.mp3")
  pygame.mixer.music.play()

# function to stop music 
def StopMusic():
  pygame.mixer.music.stop()


# GUI With Tkinter : ------------------------------------------------------------------------------------------------------------------

# Create Window :
main_window = Tk()
# Set window to open in the center of the screen 
main_window.eval('tk::PlaceWindow . center')
# play music
PlayMusic()

# set an icon to the path button 
folder_image = PhotoImage(file="file/folder.png").subsample(20, 25)


# window settings (title, geometry, icon)
main_window.title('Sweet Manager v1.0')
main_window.geometry('600x520')
main_window.resizable(False, False)
main_window.iconbitmap("file/Logo.ico")

# New frame for downloading 
download_warpper = LabelFrame(main_window, text='Download')
download_warpper.pack(fill='both', expand=YES, padx=10, pady=10)

# label
lbl1 = Label(download_warpper, text='Enter The URL :')
lbl1.grid(row=0, column=0, padx=20, pady=20)
# input the video url
link_input = Entry(download_warpper, text="url", width=57)
link_input.grid(row=0, column=1, padx=3, pady=20)
# label
lbl2 = Label(download_warpper, text='Select Path :')
lbl2.grid(row=1, column=0, padx=20, pady=20)
# Show path
path_output = Label(download_warpper, text="No Path Selected!", width=57)
path_output.grid(row=1, column=1, padx=3, pady=20)
# path button
path_button = Button(download_warpper, image=folder_image, command=getpath)
path_button.grid(row=0, column=2, padx=4, pady=20)
# download video high quality button
downloadhigh_button = Button(download_warpper, text="Video(High)", command=DownloadHigh)
downloadhigh_button.grid(row=2, column=0, padx=1, pady=20)
# download video low quality button
downloadlow_button = Button(download_warpper, text="Video(Low)", command=DownloadLow)
downloadlow_button.grid(row=2, column=1, padx=1, pady=20)
# download audio button
downloadaudio_button = Button(download_warpper, text="Audio", command=DownloadAudio)
downloadaudio_button.grid(row=2, column=2, padx=1, pady=20)


# New frame for show download info
status_warpper = LabelFrame(main_window, text='Download Status')
status_warpper.pack(fill='both', expand=YES, padx=10, pady=10)
# show downloading iindo
status = Text(status_warpper,height=20)
status.pack(pady=3, padx=3)
status.insert('1.0', """
 --------------------------------------------------------------------
    ______                                                       
   /      \                                                      
  |  $$$$$$\  ______    ______    ______   ______   ______ ____  
  | $$___\$$ /      \  /      \  /      \ |      \ |      \    \ 
  | $$    \ |  $$$$$$\|  $$$$$$\|  $$$$$$\ \$$$$$$\| $$$$$$\$$$$\ 
  | $$$$$$$\| $$  | $$| $$   \$$| $$   \$$/      $$| $$ | $$ | $$
  | $$__/ $$| $$__/ $$| $$      | $$     |  $$$$$$$| $$ | $$ | $$
   \$$    $$ \$$    $$| $$      | $$      \$$    $$| $$ | $$ | $$
    \$$$$$$   \$$$$$$  \$$       \$$       \$$$$$$$ \$$  \$$  \$$

 ---------------------------- Sweet Manager ------------------------- \n""")


# Bar Menu (open location, Exit)
menu = Menu(main_window)
file_menu = Menu(menu, tearoff=0)
file_menu.add_command(label='Open', command=OpenLocation)
file_menu.add_command(label='Exit', command=main_window.quit)
menu.add_cascade(label='File', menu=file_menu)

# bar Menu(sound off, sound on)
sound_menu = Menu(menu, tearoff=0)
sound_menu.add_command(label='Sound ON', command=PlayMusic)
sound_menu.add_command(label='Sound OFF', command=StopMusic)
menu.add_cascade(label='Sound', menu=sound_menu)
main_window.config(menu=menu)

# open window 
main_window.mainloop()
#-------------------------------------------------------------------------------------------------------------------------------------------