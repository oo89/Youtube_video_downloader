#Youtube video Downloader. 
import os
from pytube import YouTube
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
video_url = input('Enter or Copy the video url: ')
cwd = os.getcwd() 
yt = YouTube(video_url) 
title = yt.title
stream = yt.streams.get_by_itag(22)
yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download(cwd, title, 'mp4')

