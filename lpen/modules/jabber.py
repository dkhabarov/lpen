# -*- coding: utf8 -*- 
import xmpp

class Plugin:

  def __init__(self,config):
    self.config = config
    self.debug = None

  def notify(self, message, to):
    jid=xmpp.protocol.JID(self.config['xmpp_login'])
    cl=xmpp.Client(jid.getDomain(),debug=[])

    con=cl.connect()
    if self.debug and not con:
      print('Could not connect!')
      return None

    auth=cl.auth(jid.getNode(),self.config['xmpp_password'],resource="Servers")
    if self.debug and not auth:
      print('Authentication failed!')
      return None

    cl.send(xmpp.Presence(to=to,typ = 'subscribe'))
    cl.send(xmpp.Presence(to=to,typ = 'subscribed'))
    id=cl.send(xmpp.protocol.Message(to=to,body=message))
    cl.disconnect()
