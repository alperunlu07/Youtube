import youtube_dl

a="https://www.youtube.com/watch?v=B3rft973J5w&list=PL3lGdrkJu7a6yQGUgCY8aRr29yn474sxI"
ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '320',}],
    }
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([a])