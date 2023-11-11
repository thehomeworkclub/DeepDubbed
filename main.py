from elevenlabs import generate, stream, set_api_key
import os
from yt_dlp import YoutubeDL
ydl_opts = {
    'outtmpl': '%(title)s.%(ext)s',
    'quiet': 'true',
    'format': 'bestvideo+bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegVideoConvertor',
        'preferedformat': 'mp4',
    }],
}
def download():
    global ydl_opts
    with YoutubeDL(ydl_opts) as ydl:
        ydl.download([str(input("Enter URL: "))])
download()
set_api_key(os.environ['ELEVENLABS_API_KEY'])
