import RPi.GPIO as GPIO
import csv
import time
import datetime


#setup GPIO pin
sensorPin = 14
GPIO.setmode(GPIO.BCM)
GPIO.setup(sensorPin, GPIO.IN)

# used for debugging
count = 0
while count < 10:
 
 # reading voltage to the pin
 now = datetime.datetime.now()
 reading = GPIO.input(sensorPin)
 print("Reading: " +str(reading))
 
 #voltage = reading * 5.0
 voltage = reading
 
 print("Voltage: " +str(voltage))
 
 # converts voltage to temps
 temperatureC = (voltage - 0.5) * 100
 temperatureF = (temperatureC * 9.0 / 5.0) + 32.0
 
 print("Temperature in Fahrenheit: "+str(temperatureF))
 
 #assumed data format:     "tempF,hh,DD,MM,YYYY"
 #example_temp_reading = 70:10/24:04/12/2019 

 # writes to csv
 csvData = str(temperatureF)+ ","+str(now.minute)+","+str(now.hour)+","+str(now.day)+","+str(now.month)+","+str(now.year) 
 with open('temp_data.csv', 'w') as csv_File:
     writer = csv.writer(csvFile)
     writer.writerows(csvData)
   
 count+=1
 time.sleep(60)
                                
GPIO.cleanup()
