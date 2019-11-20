# -*- coding: utf-8 -*-
import smtplib
from email.mime.text import MIMEText
from email import encoders
from email.message import Message
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from django.conf import settings




def send_mail_contact (contact):  
        
    html = '''
        <html>
            <head></head>
            <body>
                
                <br>
                <h3>Contacto Alúmnica: </h3>
                <br>
                <p>
                    Nombre: %s
                </p>
                
                <p>
                    Email: %s
                </p>

                <p>
                    Teléfono: %s
                </p>
                <p>
                    Mensaje: %s
                </p>
                
            </body>
        </html>
    ''' % (contact.name,contact.email,contact.phone,contact.msg)
    send_email(html)
    print ('Email contact ok')


def send_mail_suscriber (suscriber):  
        
    html = '''
        <html>
            <head></head>
            <body>
                
                <br>
                <h3>Subscriptor Alúmnica: </h3>
                <br>
                
                <p>
                    Email: %s
                </p>
                
                
            </body>
        </html>
    ''' % (suscriber.email)
    send_email(html)
    print ('Email suscriber ok')

    

def send_email (html):
    themsg = MIMEMultipart()
    themsg['Subject'] = 'Contacto alúmnica'
    themsg['To'] = settings.TO_ADDR #", ".join(to_addr)
    themsg['From'] = settings.FROM_ADDR    
    part1 = MIMEText(html, 'html', 'utf-8')
    themsg.attach(part1)    
    server = smtplib.SMTP(settings.MAIL_SERVER)
    server.ehlo()
    server.starttls()
    server.login(settings.USERNAME_EMAIL,settings.EMAIL_PASS)
    server.sendmail(settings.FROM_ADDR, settings.TO_ADDR, str(themsg))
    server.quit()