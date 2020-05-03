var=$(./list_devices.sh)
sudo pacat --record -d $var > dump.raw
sox -t raw -r 44100 -e signed-integer -L -b 16 -c 2 dump.raw output.wav
rm dump.raw
