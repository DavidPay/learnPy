#!/usr/bin/env python
# -*- coding: utf-8 -*- 
#author: David Pay
#date: 06-26-2018  

from nntplib import NNTP
import nntplib
from time import strftime, time , localtime
from datetime import datetime, timedelta

oneDay = 24 * 60 * 60

yesterday = datetime.now() - timedelta(days=1)
#date = strftime('%y%m%d', yesterday)
#hour = strftime('%H%M%S', yesterday)

servername = 'news.gmane.org'
groupname = 'gmane.comp.python.committers'
server = NNTP(servername)

resp, count, first, last, name = server.group(groupname)
resp, overviews = server.over((last -9, last))
for id, over in overviews:
    print(id, nntplib.decode_header(over['subject']))
'''
ids = server.newnews(group, yesterday)[1]

for id in ids:
    head = server.head(id)[3]
    for line in head:
        if line.lower().startswith('subject:'):
            subject = line[9:]
            break
    body = server.body(id)[3]

    print(subject)
    print('-'*len(subject))
    print('\n'.join(body))

server.quit()
'''