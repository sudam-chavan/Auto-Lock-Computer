rom bluetooth import *
import time
import ctypes

bluetooth_device_name=”<bluetooth device name>″ #write your bluetooth device name here
print “Script running…”
while 1:
  flg=0
  #Discover nearby devices.
  nearby_devices = discover_devices(lookup_names = True)
  for addr, name in nearby_devices:
    if name == bluetooth_device_name:
      flg=1
      break
    else:
      flg=0
    #print ” %s – %s” % (addr, name)

  if flg == 0:
    #Lock the workstation
    ctypes.windll.user32.LockWorkStation()

  #delays for 1 second
  time.sleep(1)
