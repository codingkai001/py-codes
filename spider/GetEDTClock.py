"""US Naval Observatory Master Clock Time"""
from urllib.request import urlopen

for line in urlopen('http://tycho.usno.navy.mil/cgi-bin/timer.pl'):
    line = line.decode('UTF-8')
    if 'EDT' in line or 'Eastern Time' in line:
        print(line)
