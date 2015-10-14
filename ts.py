import sqlite3
from mailer import Mailer, Message


with open('pwd.txt', 'r') as f:
    pswd = f.read()

me = 'alephmelo@icloud.com'
you = 'alephbreno19@gmail.com'
iCloudSMTP = 'smtp.mail.me.com:587'
GmailSMTP = 'smtp.gmail.com:587'

conn = sqlite3.connect('database/email_data.db')
c = conn.cursor()
c.execute("SELECT email_ad FROM emails")
result = c.fetchall()


for x in result:
    message = Message(From=me, To=x[0], charset="utf-8")
    message.Subject = "Testando."
    message.Html = """ Sim, testando. """
    sender = Mailer(iCloudSMTP, use_tls=True, usr=me, pwd=pswd)
    sender.send(message)
