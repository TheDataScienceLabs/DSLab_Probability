import machine
import time

temp_sensor = machine.ADC(4)            

file = open("temp.txt", "w")            # file name, "w" stands for write
num = 12

while num>0:
  reading = temp_sensor.read_u16()      # read in sensor value
  time.sleep(0.25)   
  file.write(str(reading) + "\n")       # "\n" creates a new line in the txt file
  num -= 1                   # wait 0.25 seconds before proceeding

file.close()
