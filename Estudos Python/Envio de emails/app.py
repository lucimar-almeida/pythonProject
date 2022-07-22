import pandas as pd
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib


clientes = pd.read_excel(
    'E:\Github\pythonProject\Estudos Python\Envio de emails\clientes.xlsx')

for index, cliente in clientes.iterrows():
    #print(cliente['nome'], cliente['email'])
    msg = MIMEMultipart()
    msg['Subject'] = 'Email da PycodeBr'
    msg['From'] = 'lucimar.a.s123@gmail.com'
    msg['To'] = cliente['email']
    message = f"Olá {cliente['nome']}, você recebeu um email da PycodeBr!"
    msg.attach(MIMEText(message, 'plain'))

    server = smtplib.SMTP('smtp.gmail.com', port=587)
    server.starttls()
    server.login('lucimar.a.s123@gmail.com', 'las261187!')
    server.sendmail(msg['from'], msg['To'], msg.as_string())
    server.quit()
