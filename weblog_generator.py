import time
import datetime
from datetime import timedelta
import random
from random import randint
from randome import randrange

# Log example (as in https://en.wikipedia.org/wiki/Common_Log_Format)
# 127.0.0.1 user-identifier frank [10/Oct/2000:13:55:36 -0700] "GET /apache_pb.gif HTTP/1.0" 200 2326
# client_address client_rfc user_id [%d/%b/%Y:%H:%M:%S %z] "request" http_retured_status_code returned_item_size

# Generate a randome date between two specific dates
def random_date(start, end):
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = randrange(int_delta)
    return start + timedelta(seconds=random_second)

# pick a random row from file
def random_line(file):
    line = next(file)
    for num, aline in enumerate(file):
      if random.randrange(num + 2): continue
      line = aline
    return line

timestr = time.strftime("%Y%m%d-%H%M%S")
# num_clicks = 500

otime = datetime.datetime(2014, 10, 10, 0, 0, 0)
timestr =  time.strftime("%Y%m%d-%H%M%S", otime.timetuple())

f = open('access_log_' + timestr + '.log','w')

user_agents_dir = "user_agents/"
#stock_list = [x[0] for x in os.walk(statspath)]
for each_dir in 

files = os.

# IPv4 addresses are canonically represented in dot-decimal notation, 
# which consists of four decimal numbers, each ranging from 0 to 255, separated by dots
# ip[0] = 10..255 (just because we don't want ips like 0.145.12.155)
ip= randint(10,255) + '.' + randint(0,255) + '.' + randint(0,255) + '.' + randint(0,255)


single_visit_ip=["10.181.198.78", ]
referers=["-","http://www.casualcyclist.com","http://bestcyclingreviews.com/top_online_shops","http://bleater.com","http://searchengine.com"]
resources=["/handle-bars","/stems","/wheelsets","/forks","/seatposts","/saddles","/shifters","/Store/cart.jsp?productID="]
useragents=["Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)","Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1944.0 Safari/537.36","Mozilla/5.0 (Linux; U; Android 2.3.5; en-us; HTC Vision Build/GRI40) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1","Mozilla/5.0 (iPad; CPU OS 6_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10A5355d Safari/8536.25","Mozilla/5.0 (Windows; U; Windows NT 6.1; rv:2.2) Gecko/20110201","Mozilla/5.0 (Windows NT 5.1; rv:31.0) Gecko/20100101 Firefox/31.0","Mozilla/5.0 (Windows; U; MSIE 9.0; WIndows NT 9.0; en-US))"]

# Generate times during the day for which we click
times=[]
for i in xrange(0,num_clicks):
       seconds = datetime.timedelta(seconds=random.randint(0,86399))
       times.append(seconds)

# Then, sort them. We do this because we want a random distribution of clicks during the day but since random() is
# not sorted, we sort them afterwards.
times.sort()

# Now we randomly pick other columns, combine them one by one with our sorted list of times and write it to a file
for i in xrange(0,num_clicks):
        uri = random.choice(resources)
        if uri.find("Store")>0:
                uri += `random.randint(1000,1500)`
        ip = random.choice(ips)
        useragent = random.choice(useragents)
        referer = random.choice(referers)
        f.write('%s - - [%s] "GET %s HTTP/1.0" 200 %s "%s" "%s"\n' % (random.choice(ips),(otime+times[i]).strftime('%d/%b/%Y:%H:%M:%S %z'),uri,random.randint(2000,5000),referer,useragent))
