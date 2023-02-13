

from pytube import YouTube
def download_audio(url):
    yt = YouTube(url)
    audio_name = yt.title
    yt.streams.filter(only_audio=True).first().download("audio", f"{audio_name}.mp3")
    return f"{audio_name}.mp3"
