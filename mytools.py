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

  ------------------------ Sweet Manager --------------------------                                                                                                                                                                                        
  """)

from pytube import YouTube
from time import sleep

class DownloadTools:
  
  def DownloadHigh(link):
    link = input("output a link : ")
    yt = YouTube(link)
    stream = yt.streams.get_highest_resolution()
    stream.download(r"C:\Users\Abderrahmane\Downloads\Downloads")
    print("download succesfuly :)")
    sleep(3)

  def DownloadLow(link):
    link = input("output a link : ")
    yt = YouTube(link)
    stream = yt.streams.get_lowest_resolution()
    stream.download(r"C:\Users\Abderrahmane\Downloads\Downloads")
    print("download succesfuly :)")
    sleep(3)

  def DownloadAudio():
    link = input("output a link : ")
    yt = YouTube(link)
    stream = yt.streams.get_audio_only()
    stream.download(r"C:\Users\Abderrahmane\Downloads\Downloads")
    print("download succesfuly :)")
    sleep(3)