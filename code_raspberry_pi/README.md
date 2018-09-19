# Raspberry PI Setup

## OS
Official Raspbian is used

## Setup
### Enable i2c
```
sudo raspi-config
```

### Script on boot
```
sudo crontab -e

# then append the following at the end
# ensure the sh script is 'executable'
# chmod +x my_start_script.sh
@reboot /home/pi/__my__start__script.sh
```

