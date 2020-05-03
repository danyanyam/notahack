sudo chmod +x record.sh
sudo chmod +x to_wav.sh

pacmd list | grep ".monitor" > devices.txt
python find_device.py
rm devices.txt
