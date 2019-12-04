import RPi.GPIO as GPIO
sensorPin = 14



GPIO.setmode(GPIO.BCM)
GPIO.setup(sensorPin, GPIO.IN)

count = 0
while count < 10:
 reading = GPIO.input(sensorPin)
 print("Reading: " +str(reading))
 
 #voltage = reading * 5.0
 voltage = reading
 
 print("Voltage: " +str(voltage))
 
 temperatureC = (voltage - 0.5) * 100
 
 
 temperatureF = (temperatureC * 9.0 / 5.0) + 32.0
 print("Temperature in Fahrenheit: "+str(temperatureF))
 count+=1
                                
GPIO.cleanup()
