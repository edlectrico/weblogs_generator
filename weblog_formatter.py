import pandas as pd
import re

f = open('out_log.log', 'r')

df = pd.DataFrame(columns = ['IP','Date','Request','Response HTTP','Response in bytes','Referer','User Agent'])

for line in f:
  ip = re.search(r'\d{1,255}\.\d{1,255}\.\d{1,255}\.\d{1,255}', line).group()
  date = line.split('[', 1)[1].split(']')[0]
  request = line.split('"', 1)[1].split('"')[0]
  response_http = line.split('" ', 1)[1].split(' ')[0]
  response_bytes = line.split('" ')[1].split(' ')[1]
  referer = line.split(' "')[2].replace('"', '')
  user_agent = line.split(' "')[3].replace('"', '').replace(',', ' ')

  df.append({'IP':str(ip),'Date':str(date), 'Request':str(request), 'Response HTTP':str(response_http), 'Response in bytes':str(response_bytes), 'Referer':str(referer), 'User Agent':str(user_agent),}, ignore_index = True)

  df.loc[len(df)+1]=[ip, date, request, response_http, response_bytes, referer, user_agent]

  # print 'Inserting in df[' + str(len(df)) + ']'

df.to_csv('weblogs.csv')
print df

