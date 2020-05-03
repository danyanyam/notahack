sudo chmod +x record.sh

pacmd list | grep ".monitor" > devices.txt
python find_device.py
rm devices.txt
