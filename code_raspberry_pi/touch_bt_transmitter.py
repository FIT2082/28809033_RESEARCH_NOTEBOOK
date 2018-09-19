import sys
import time
import subprocess

import Adafruit_MPR121.MPR121 as TouchSensor

sensor = TouchSensor.MPR121()

def initBluetooth():
    return 0

    # Programatic way of initializing bluetooth in python
    # At the moment we'll use a start script
    onCommand = "sudo hciconfig hci0 up"
    intervalCommand = "sudo hcitool -i hci0 cmd 0x08 0x0006 00 A0 00 FF 03 00 00 00 00 00 00 00 00 07 00"
    startCommand = "sudo hcitool -i hci0 cmd 0x08 0x000a 01"

    assert subprocess.call(onCommand, shell=True) == 0, "on Command Failed"
    assert subprocess.call(intervalCommand, shell=True) == 0, "interval Command Failed"
    assert subprocess.call(startCommand, shell=True) == 0, "start Command Failed"


def advertiseBluetoothSensorError():
    """
    :return:
    """
    command = """sudo hcitool -i hci0 cmd 0x08 0x0008 1c 02 01 06 03 03 aa fe 14 16 aa fe 10 00 03 6d 79 70 2e 6d 65 3f 73 65 6e 73 65 72 72 00 00 00"""
    p1 = subprocess.call(command, shell=True)
    assert p1 == 0, "Non 0 Exit Code"
    return p1


def advertiseBluetooth(index):
    """
    :param index: string of hex which maps to 0-9 in Ascii.
    :return: Exit code from shell command. 0 = success, else fail.
    """

    print(index)

    touched_sensor = index
    print("Advertising {}".format(touched_sensor.decode("hex")))
    command = """sudo hcitool -i hci0 cmd 0x08 0x0008 1d 02 01 06 03 03 aa fe 15 16 aa fe 10 00 03 68 65 6c 6c 6f 77 6f 72 6c 64 2e 6d 65 3f {} 00 00""".format(
        touched_sensor)
    p1 = subprocess.call(command, shell=True)
    assert p1 == 0, "Non 0 Exit Code"
    return p1



def checkSensor():
    """
    :return: check if the sensor is wired correctly and communication is valid.
    """
    if not sensor.begin():
        print('Error initializing MPR121.  Check your wiring!')
        # TODO: send error message advertising bluetooth
        sys.exit(1)



checkSensor()

# We can assume sensor works now
last_touched = sensor.touched()
while True:
    current_touched = sensor.touched()
    for i in range(12):
        # Each pin is represented by a bit in the touched value.  A value of 1
        # means the pin is being touched, and 0 means it is not being touched.
        pin_bit = 1 << i
        # First check if transitioned from not touched to touched.
        if current_touched & pin_bit and not last_touched & pin_bit:
            asciiZero = 48
            hexCode = hex(asciiZero + i)
            advertiseBluetooth(str(hexCode)[2:])
            print('{} touched'.format(i))

    # Reset the touch point
    last_touched = current_touched
    time.sleep(0.1)
