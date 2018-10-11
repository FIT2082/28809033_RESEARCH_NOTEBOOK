Week 9

##  Autostart Beacon 

Any linux code can be run on autostart of the Raspberry PI using crontab. 

```
crontab -e 
```
I added the startup script to run on reboot

I also noticed I'd added the script to the user account, not the sudo account. I had to run

```
sudo crontab -e
```

Then added the line below at the end.

```
@reboot ./dir/to/startup.sh
```

However, I noticed that the script wasn't starting up and running, hence the beacon didn't start transmitting. It was very hard to debug it as there were no logs. It was eventually fixed by adding 

```
@reboot sleep(20) && ./dir/to/startup.sh
```

The 'sleep' so that the bluetooth driver loads and it works out.

Debugging it adding sleep to crontab and also run as sudo 


## Capacitive Touch Sensor and Beacon 

Touch sensor polling and advertising made the combination possible. The python script runs the linux commands to change the bluetooth advertising data. 

## Reflection
This week had been extremely challenging and took a toll on everything as debugging was hard and the times were tough during the semester. 



