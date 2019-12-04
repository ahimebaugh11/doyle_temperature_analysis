#first creation of analysis file

import csv

with open('temp_data.csv') as csv_file:
  csv_reader = csv_reader(csv_file, delimiter=',')
  line_count = 0
  data = []
  for row in csv_reader:
    data.append(row)
    line_count += 1
high_temp = data[0]
low_temp = data[1]
for x in data:
  if x[0] > high_temp:
    #determines highest temp in total data range
    high_temp = x[0]
  #determines lowest temp in total data range
  if x[0] < low_temp:
    low_temp = x[0]
      





























