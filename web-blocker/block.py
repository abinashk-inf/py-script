#!/usr/bin/python3
import datetime as dt
'''
Only for linux systems.
change host to /etc/hosts
This script will block the mentioned sites between the time am and pm. The date does not matter since only time is extracted
'''
sites=['www.facebook.com','www.9gag.com']
loopback='127.0.0.1'
host='host'
now=dt.datetime.now()
am=dt.datetime(2017,12,7,9,0,0,0)
pm=dt.datetime(2017,12,7,21,23,0,0)
while 1:
    if am.time()<now.time()<pm.time():
        with open(host,'r') as fp:
            data=fp.read()
        for site in sites:
            if site in data:
                pass
            else:
                data=data+loopback+' '+site+'\n'
        with open(host,'w') as fp:
            fp.write(data)
    else:
        with open(host,'r') as fp:
            data=fp.readlines()
        for line in data:
            for site in sites:
                if site in line:
                    data.remove(line)
                else:
                    pass
        with open(host,'w') as fp:
            for i in data:
                fp.write(i)

