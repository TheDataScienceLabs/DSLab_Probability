import machine
import time

temp_sensor = machine.ADC(4)

conversion_factor = 3.3 / (65535)
file = open("temp.txt", "w")
num = 12

while num>0:
  reading = temp_sensor.read_u16()
  file.write(str(reading) + "\n")
  num -= 1
  time.sleep(0.25)

file.close()