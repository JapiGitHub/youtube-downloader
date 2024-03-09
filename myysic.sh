#/bin/bash

# Ensure URL is provided
if [ -z "$1" ]; then
  echo "Usage: $0 <URL>"
  exit 1
fi

pytube "$1" -t ~/Music/

FILENAME=$(basename $(echo $1 | cut -d'&' -f1) .mp4)

ffmpeg -i [i need the output files name here] -vn -ab 128k -ar 44100 -y UGK.mp3