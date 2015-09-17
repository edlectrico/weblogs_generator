import pandas as pd
from geoip import geolite2
import sys

df = pd.DataFrame.from_csv('weblogs.csv')

geo_df = pd.DataFrame(columns = ['IP', 'Country', 'Continent', 'Timezone'])

ips = df['IP'].get_values()

for ip in ips:
  try:
    match = geolite2.lookup(ip)
    if (match is not None):
      geo_df.loc[len(geo_df)+1]=[ip, match.country, match.continent, match.timezone]
      # geo_df.append({'Country':match.country, 'Continent':match.continent, 'Timezone':match.timezone}, ignore_index = True)
    else:
      geo_df.loc[len(geo_df)+1]=[ip, 'N/A', 'N/A', 'N/A',]
      # geo_df.append({'Country':'N/A', 'Continent':'N/A', 'Timezone':'N/A'}, ignore_index = True)
  
  except KeyboardInterrupt:
    print 'KeyboardInterrupt exception raised! Writing to file...'
    geo_df.to_csv('geo_weblogs.csv')
    sys.exit()
    
geo_df.to_csv('geo_weblogs.csv')
