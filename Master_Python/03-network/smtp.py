import smtplib

s = smtplib.SMTP('192.168.1.107', 25)

try:
    m = '\nThis is a message'
    s.sendmail('chris09.yu@gmail.com', 'chris09.yu@msa.hinet.net', m)
    print('Finished sending message')
except Exception as e:
    print('Unable to send message:', e)

s.quit()
