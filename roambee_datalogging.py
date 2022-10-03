#!/usr/bin/env python

import datetime
import serial
import time



serial_port = '/dev/cu.usbmodem11201'
serial_baud = 115200
log_dir = "log-data/"

#create unique file name every time
file_name = 'output_'+datetime.datetime.now().strftime("%y-%m-%d %h:%m:%s")+'.txt'
file_filter_name = 'output_filter_'+datetime.datetime.now().strftime("%y-%m-%d %h:%m:%s")+'.txt'


fid=open(log_dir+file_name,'ab')
fid1=open(log_dir+file_filter_name,'ab')


filter_string = '#@>'


#provide you serial port det
ser = serial.Serial( serial_port, serial_baud , timeout = 10)
# ser = serial.Serial(
#         port='/dev/cu.usbmodem1201',
#         baudrate=115200,
#         parity=serial.PARITY_NONE,
#         stopbits=serial.STOPBITS_ONE,
#         bytesize=serial.EIGHTBITS,
#         timeout=10
# )

loop = 1; #loop until you hit something 
while loop:
    try:
        if(ser == None):
            ser = serial.Serial( serial_port, serial_baud , timeout = 10)
        else:
            x=ser.readline()
        #filter the string here and store to the filter file
        print('{:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.now()))
        print(x)
        time.sleep(0.01)
        fid.write(bytes(datetime.datetime.now().strftime("%y-%m-%d %H:%M:%S")+": ",'ascii'))
        fid.write(x)
        if x.decode().startswith(filter_string):
            fid2.write(x)

    except Exception as e:
        print("**** Device disconnected or some error *****")
        fid.write(bytes(datetime.datetime.now().strftime("%y-%m-%d %H:%M:%S")+": "+"DeviceDisconnted or some error - ",'ascii'))
        print(e)
        #loop=0;
        #ser.close()
        ser = None
        #quit()
