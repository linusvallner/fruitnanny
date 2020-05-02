#!/usr/bin/python
import sys
from lifxlan import LifxLAN

def main():
  num_lights = None
  function = None

  if len(sys.argv) < 2:
    function = sys.argv[1]
  else:
    num_lights = int(sys.argv[1])
    function = sys.argv[2]

  # instantiate LifxLAN client, num_lights may be None (unknown).
  # In fact, you don't need to provide LifxLAN with the number of bulbs at all.
  # lifx = LifxLAN() works just as well. Knowing the number of bulbs in advance
  # simply makes initial bulb discovery faster.
  lifx = LifxLAN(num_lights)

  # get fruitnanny device
  device = lifx.get_device_by_name("Fruitnanny IR")

  if device != None:
    if function in 'on':
      set_infrared_on(device)
    elif function in 'off':
      set_infrared_off(device)
    else:
      get_device_status(device)
  else:
    print("\nCould not get lifx device\n")

def set_infrared_on(light):
  light.set_infrared(65535)

def set_infrared_off(light):
  light.set_infrared(0)

def get_device_status(light):
  status = light.get_infrared()
  if status:
    print("1")
  else:
    print("0")

if __name__=="__main__":
  main()

