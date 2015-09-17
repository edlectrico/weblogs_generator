from datetime import datetime
import os
import time
from random import randint, choice
import requests
import glob

import utils as u

timestr = time.strftime("%Y%m%d-%H%M%S")
otime = datetime(2015, 9, 11, 10, 39, 40)
timestr =  time.strftime("%Y%m%d-%H%M%S", otime.timetuple())

http_responses = [200, 400, 403, 404, 500]

referers = 	['http://www.rankia.com/', 
		'http://www.elblogsalmon.com/', 
		'http://www.finanzas.com/',
		'http://www.bankimia.com/',
		'http://www.elconfidencial.com/mercados/',
		'http://www.invertia.com/',
		'http://cincodias.com/',
		'http://www.expansion.com/',
		'http://www.eleconomista.es/',
		'https://www.facebook.com/',
		'https://www.twitter.com/',
		'https://www.linkedin.com/'
		]

initial_date = datetime.strptime('1/1/2015 1:00 PM', '%m/%d/%Y %I:%M %p')
final_date = datetime.strptime('9/30/2015 6:00 PM', '%m/%d/%Y %I:%M %p')

# Get all resources from specified website
page = requests.get('https://www.bbva.es/particulares/index.jsp')
# tree = html.fromstring(page.text)
source = page.text
resources = []
a = source.split('href="')
for href in a:
  resources.append(href.split('"')[0])
resources = resources[1:]

user_agents_dir = "user_agents/"
useragents_list = glob.glob(user_agents_dir + '*.txt')
all_user_agents = []
for file in useragents_list:
    all_user_agents.append(open(file, 'r').readlines())

# f = open('access_log_' + timestr + '.log','w')
f = open('out_log.log', 'w')

while True:
  ip = str(randint(10,255)) + '.' + str(randint(0,255)) + '.' + str(randint(0,255)) + '.' + str(randint(0,255))
  date = str(u.random_date(initial_date, final_date))
  date = date.replace(" ", ":").replace("-", "/").split(' ')[0]
  resource = str(choice(resources))
  request = "GET " + resource
  # response = str(random.choice(http_responses)) # [200, 400, 403, 404, 500]
  response = str(u.weighted_choice([	
				(http_responses[0], 90), 
				(http_responses[1], 10), 
				(http_responses[2], 40), 
				(http_responses[3], 30), 
				(http_responses[4], 50)
			     ]))

  response_bytes = str(randint(2000,5000))
  # referer = str(choice(referers))
  referer = str(u.weighted_choice([
			(referers[0], 20),
                        (referers[1], 40),
                        (referers[2], 50),
                        (referers[3], 30),
                        (referers[4], 30),
                        (referers[5], 20),
                        (referers[6], 50),
                        (referers[7], 40),
                        (referers[8], 40),
                        (referers[9], 15),
                        (referers[10],15),
                        (referers[11],15),
			]))
  user_agent = str(choice(choice(all_user_agents))).split("\n")[0]

  # print ip, date, request, response, response_bytes, referer, user_agent
  f.write(ip + ' -' + ' - '  +'[' + date + ']' + ' ' + '"' + request + '"' + ' ' + response + ' ' + response_bytes + ' ' + '"' + referer + '"' + ' ' + '"' + user_agent + '"' + '\n')
