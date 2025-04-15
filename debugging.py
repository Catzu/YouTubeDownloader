from pytubefix import YouTube

try:
    yt = YouTube("https://www.youtube.com/watch?v=2lAe1cqCOXo")
    stream = yt.streams.get_highest_resolution()
    stream.download()
    print("Download complete!")
except Exception as e:
    print(f"Error: {e}")