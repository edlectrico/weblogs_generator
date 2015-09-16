import pandas
import re

f = open('out_log.log', 'r')

for line in f:
  ip = re.search(r'\d{1,255}\.\d{1,255}\.\d{1,255}\.\d{1,255}', line).group() 
  date = line.split('[', 1)[1].split(']')[0]
  request = line.split('"', 1)[1].split('"')[0]
  response_http = line.split('" ', 1)[1].split(' ')[0]
  response_bytes = line.split('" ')[1].split(' ')[1]

  print ip, date, request, response_http, response_bytes

