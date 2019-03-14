import smtplib
from email.mime.text import MIMEText
from PRIVATE_INFO import credential


# send email via gmail, remember to lower google account security to use this function
def send_email(to='', subject='IPO boutique', message=str('')):
    try:
        smtp = smtplib.SMTP('smtp.gmail.com', 587)
        smtp.ehlo()  # say Hello
        smtp.starttls()  # TLS 사용시 필요
        smtp.login(credential[0], credential[1])
        msg = MIMEText(message)
        msg['Subject'] = subject
        msg['To'] = to
        smtp.sendmail(credential[0], to, msg.as_string())
        smtp.quit()

        print(
            f'####Email Success####\n To: {to}\n Subject: {subject} \n Message: {message}'
        )
    except:
        print('Email Error')

