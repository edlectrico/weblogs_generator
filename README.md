# weblogs_generator
A simple weblog generator Python script. The project contains:
- weblog_generator.py: A script which generates random values for logs and stores them in an .log output file.
- weblog_formatter.py: A script which uses the .log as input and generates a .csv file using pandas.
- utils.py: Several functions used by weblog_generator.py.
- ip_locator.py: To geolocate the IPs using the geoip lib.

To generate the random weblogs just run:
```
$ python weblog_generator.py
```
This command will generate an out_log.log file. Then execute:
```
$ python weblog_formatter.py
```
So now you have a weblogs.csv file in your project folder.

To cancel both scripts you can use Ctrl+C. Otherwise the random generation of the logs won't ever end! 


Remember to install 'pandas' and 'requests' Python packages:
```
$ pip install pandas
$ pip install requests
$ pip install geoip
$ pip install geolite2
```
