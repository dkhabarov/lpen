#-*- coding: utf8 -*-
import smtplib
from email.mime.text import MIMEText

class Plugin:

  def __init__(self,config):
    self.config = config
    self.debug = None
  
  def notify(self, message, to):

    try:
      msg = MIMEText(message)
      msg['Subject'] = "Your password has expired!"
      msg['From'] = self.config.get('smtp_auth_user')
      msg['To'] = to
      transport = smtplib.SMTP(self.config.get('smtp_server_addr'), self.config.get('smtp_server_port'))
      if self.debug:
        transport.set_debuglevel(1)
      transport.ehlo
      transport.starttls()
      transport.login(self.config.get('smtp_auth_user'), self.config.get('smtp_auth_password'))
      transport.sendmail(self.config.get('smtp_auth_user'), to, msg.as_string())
      transport.quit()
    except:
      if self.debug:
        print("Error, while sending message for %s" % to)
        return None
