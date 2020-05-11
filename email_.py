import smtplib
conn = smtplib.SMTP('smtp.gmail.com', 587)
conn.ehlo()
conn.starttls()

conn.login('sender@gmail.com', 'pass')
conn.sendmail('sender@gmail.com','reciever@gmail.com','hi from python!!!')
conn.quit()