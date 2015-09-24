# weblogs_generator
A simple weblog generator Python script. The project contains:
- weblog_generator.py: A script which generates random values for logs and stores them in an .log output file.
- weblog_formatter.py: A script which uses the .log as input and generates a .csv file using pandas.
- utils.py: Several functions used by weblog_generator.py.
- ip_locator.py: To geolocate the IPs using the geoip lib.

To generate the random weblogs just run:
```
$ python weblog_generator.py <mm/dd/yyyy>
```
For example:
```
$ python weblog_generator.py 09/24/2015
```
If you want to use random dates (otherwise it uses random ours of the given date) uncomment the lines under the referer array declaration). 

This command will generate an out_log.log file. Then execute:
```
$ python weblog_formatter.py
```
So now you have a weblogs.csv file in your project folder.

To cancel both scripts you can use Ctrl+C. Otherwise the random generation of the logs won't ever end! 

## Installed packages
Obviously you need Python to run the scripts. Besides, pip is required if you need to install the packages listed below (geoip and geolite2 are just needed for the ip geolocation script):
```
$ pip install pandas
$ pip install requests
$ pip install geoip
$ pip install geolite2
```
