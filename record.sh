var=$(./list_devices.sh)
sudo pacat --record -d $var > dump.raw
sox -t raw -r 44100 -e signed-integer -L -b 16 -c 2 dump.raw output.wav
ffmpeg -i output.wav -ac 1 -ar 16000 -acodec pcm_s16le ffmpeg_output.wav
rm dump.raw output.wav
