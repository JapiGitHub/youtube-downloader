
import os
import sys
from pytube import YouTube
import subprocess

print(YouTube(sys.argv[1]).streams[0].title)