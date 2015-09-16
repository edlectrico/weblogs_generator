import pandas
import re

f = open('out_log.log', 'r')

for line in f:
  ip = re.search(r'\d{1,255}\.\d{1,255}\.\d{1,255}\.\d{1,255}', line).group()
  print ip

