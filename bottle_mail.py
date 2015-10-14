from bottle import route, run, template, request
from bs4 import BeautifulSoup
import requests
import re
import sqlite3
from mailer import Mailer, Message

'''
url = "http://www.packtpub.com/packt/offers/free-learning"  # Url to be loaded.
r = requests.get(url)  # Using requests to get content.
data = r.text  # Take to plain text into data var.
soup = BeautifulSoup(data, "html5lib")
title = soup.find('div', class_='dotd-title').contents[1].string
desc = soup.find('div', class_='dotd-main-book-summary float-left'
                 ).contents[7].string
title = re.sub('\s+', ' ', str(title))
desc = re.sub('\s+', ' ', str(desc))


# Start the emailing part
me = 'alephmelo@icloud.com'
you = 'alephbreno19@gmail.com'
iCloudSMTP = 'smtp.mail.me.com:587'
GmailSMTP = 'smtp.gmail.com:587'

message = Message(From=me, To=you, charset="utf-8")
message.Subject = "%s." % title
message.Html = """ %s """ % desc
sender = Mailer(iCloudSMTP, use_tls=True, usr=me, pwd='')
sender.send(message)
'''


@route('/')
def index():
    conn = sqlite3.connect('database/email_data.db')
    c = conn.cursor()
    c.execute("SELECT id, email_ad FROM emails")
    result = c.fetchall()
    c.close()
    output = template('templates/index.tpl', rows=result)
    return output


@route('/new', method='GET')
def new_item():
    if request.GET.get('save', '').strip():
        new = request.GET.get('email').strip()
        conn = sqlite3.connect('database/email_data.db')
        c = conn.cursor()
        c.execute("INSERT INTO emails (email_ad) VALUES (?)", [new])
        new_id = c.lastrowid
        conn.commit()
        c.close()
        return '<p>The new email was placed with the number %s</p>' % new_id
    else:
        return template('templates/index.tpl')
run(reloader=True)
