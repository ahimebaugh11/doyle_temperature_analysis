
# MUST pip install matplotlib

import csv
import time
import matplotlib.pyplot as plt 

# reads in data from the CSV and removes the top label field
with open('testdata.csv') as csv_file:
    rdr = csv.reader(csv_file, delimiter=',')
    line_count = 0
    data = []
    for row in rdr:
        data.append(row)
        line_count += 1
data.remove(data[0])


print("====================================================================")
print("===========WELCOME TO THE DOYLE HALL TEMPERATURE ANALYZER===========")
print("====================================================================")
print("Which date range would you like to see the low, high, and average of?")
print("Please use the following format - hh/ddd/yyyy") 


# Receives user input and parses for pertinent info
user_input = input("First Date: ") 
#user_input = "12/256/2019"
hour1 = int(user_input[0:2])
day1 = int(user_input[3:6])
year1 = int(user_input[7:])
user_input = input("Second Date: ") 
#user_input = "23/321/2019"
hour2 = int(user_input[0:2])
day2 = int(user_input[3:6])
year2 = int(user_input[7:])


# Pointless showy calculating code :D
print("===========================CALCULATING==============================")
time.sleep(.2)
print("10%")
time.sleep(.2)

range = []
for x in data:

    # this mess is for finding data within the specified range
    if int(x[3]) >= year1 and int(x[3]) <= year2:
        if int(x[2]) >= day1 and int(x[2]) <= day2:
            if (int(x[1]) > hour1 and int(x[2]) == day1):
                range.append(x)
            
            elif(int(x[1]) < hour2 and int(x[2]) == day2):
                range.append(x)

            elif(int(x[1]) < hour1 and int(x[2]) == day1):
                continue
            elif(int(x[1]) > hour2 and int(x[2]) == day2):
                continue
            else:
                range.append(x)

print("25%")
time.sleep(.2)
print("50%")


# Initiates variables for analysis
low = int(range[0][0])
high = int(range[0][0])
average = 0
total_temp = 0
count = 0
x_axis = []
y_axis = []

for x in range:

    # Calculates final time for x-axis on the graph and adds temp to y axis
    final_time = int(x[3])*365 + int(x[2]) + int(x[1])*.01
    x_axis.append(final_time)
    y_axis.append(int(x[0]))

    # used for calcing average
    count += 1
    total_temp += int(x[0])

    # determine overall high and low
    if int(x[0]) > high:
        high = int(x[0])
    if int(x[0]) < low:
        low = int(x[0])
                
average = total_temp/count
                
time.sleep(.2)
print("80%")

# Graph plotting code
plt.plot(x_axis, y_axis, label = "Temperature over time") 
plt.xlabel('Time (Derived from Year x 365 + Day + Hour/100)') 
plt.ylabel('Temperature (F)') 
plt.title('Temperatures over the given time range') 
#plt.legend() 







time.sleep(.2)
print("100%")
print("=============================COMPLETE===============================")

# Showing the data to the user
print("High Temp for this range: "+str(high))
print("Low Temp for this range: "+str(low))
print("Average Temp for this range: "+str(average))
plt.show() 




























