
import os
import sys
from pytube import YouTube
import subprocess
import re


def convert_to_mp3(input_file, output_file):
    cmd = f'ffmpeg -i "{input_file}" -vn -ab 128k -ar 44100 -y "{output_file}"'
    subprocess.call(cmd, shell=True)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 script.py <YouTube URL>")
        sys.exit(1)

    #title = YouTube(sys.argv[1]).streams[0].title
    title = YouTube(sys.argv[1]).streams[0].title.replace(" ", "_") #removes whitespace and creates title
    
    #sanitize non-ascii chars if needed
    #title = re.sub(r'[^\x00-\x7F]+', '', title)

    print("")
    print(title)
    print("")

    path = os.path.expanduser(f'~/Music/steve-balmer/{title}.mp3')

    downloaded_file = YouTube(sys.argv[1]).streams.first().download()

    convert_to_mp3(downloaded_file, path)
    
    #keep the music video if this is commented
    #os.remove(downloaded_file) # Remove the original file after conversion


# $  mocp     starts the player

# jos koitat liian paljon, ni tulee tollanen errori
#  json@isomorko  ~/projects/youtube-donwloader  python3 filenamehack.down.py https://youtu.be/3wtbPPAZZx8
# Traceback (most recent call last):
#   File "/usr/lib/python3.10/http/client.py", line 592, in _read_chunked
#     value.append(self._safe_read(chunk_left))
#   File "/usr/lib/python3.10/http/client.py", line 633, in _safe_read
#     raise IncompleteRead(data, amt-len(data))
# http.client.IncompleteRead: IncompleteRead(1180 bytes read, 31574 more expected)

# During handling of the above exception, another exception occurred:

# Traceback (most recent call last):
#   File "/home/json/projects/youtube-donwloader/filenamehack.down.py", line 18, in <module>
#     title = YouTube(sys.argv[1]).streams[0].title.replace(" ", "_") #removes whitespace and creates title
#   File "/home/json/.local/lib/python3.10/site-packages/pytube/__main__.py", line 295, in streams
#     self.check_availability()
#   File "/home/json/.local/lib/python3.10/site-packages/pytube/__main__.py", line 210, in check_availability
#     status, messages = extract.playability_status(self.watch_html)
#   File "/home/json/.local/lib/python3.10/site-packages/pytube/__main__.py", line 102, in watch_html
#     self._watch_html = request.get(url=self.watch_url)
#   File "/home/json/.local/lib/python3.10/site-packages/pytube/request.py", line 54, in get
#     return response.read().decode("utf-8")
#   File "/usr/lib/python3.10/http/client.py", line 460, in read
#     return self._read_chunked(amt)
#   File "/usr/lib/python3.10/http/client.py", line 598, in _read_chunked
#     raise IncompleteRead(b''.join(value))
# http.client.IncompleteRead: IncompleteRead(949939 bytes read)