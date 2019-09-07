# Youtube Video İndirme
### Kütüphanenin kurulum için
    pip install youtube-dl
<br>
<h4> Örnek kullanımı

```python
import youtube_dl

a=input("enter url ")
ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '320',}],
    }

with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([a])
```
<br>
<h4> Sadece Video olarak indirmede herhangi bir sorunla karşılaşmadım ama indirilen videoyu mp3 formatına çevirmeye çalışırken şöyle bir hata aldım.
    DownloadError: ERROR: ffprobe or avprobe not found. Please install one.
<br>
<h4> Hatanın çözümü için şu videoyu izleyebilirsiniz 
https://www.youtube.com/watch?v=ObuBysxtv9M
<br>
<h4> yada şu adresteki programı sisteminiz için uygun olan versiyonunu idirebilirsiniz.
https://ffmpeg.zeranoe.com/builds/
<h4> indirdiğiniz dosyayı açıp /bin klasörü içerisindeki "ffmpeg.exe", "ffplay.exe", "ffprobe.exe" dosyalarını "C:\Users\<User Name>\AppData\Local\Programs\Python\Python36\Scripts" klasörü içerisine kopyalayabilirsiniz.
<br>
<h5> Bu kütüphane ile babamın sayesinde tanıştım. Arabada dinlek için istek şarkılarını yazılım ile indirmeye çalışırken bu kütüphaneyi keşfettim. Youtube daki videoları çalma listesi olarak da indirebilirsiniz.


# Youtube Video Downloader
### Installation of the library
    pip install youtube-dl
<br>
<h4> Sample usage

```python
import youtube_dl

a=input("enter url ")
ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '320',}],
    }

with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([a])
```
<br>
<h4> if you get an error like this
    DownloadError: ERROR: ffprobe or avprobe not found. Please install one.
<br>
<h4> Watch this video to resolve the error
https://www.youtube.com/watch?v=ObuBysxtv9M
<br>

