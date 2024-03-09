from pytube import YouTube
#YouTube('https://youtu.be/32epQgWiGJo').streams.first().download()
yt = YouTube('http://youtube.com/watch?v=32epQgWiGJo')
yt.streams.filter(progressive=True, file_extension='mp3').order_by('resolution').desc().first().download()