#!/usr/bin/env python
# -*- coding: utf-8 -*-
import spwd, sys, time, yaml, socket, os

def main():
	config = None
	plugins = {}
	try:
		config = yaml.load(open('/etc/lpen/lpen.conf.yaml'))
	except IOError as errstr:
		print('Can\'t load config file: %s' %errstr)
		sys.exit(1)

	if not config.has_key('servername') or len(config['servername']) == 0:
		servername = socket.getfqdn(socket.gethostname())
	else:
		servername = config['servername']
	
	users = None
	try:
		with open(config['user_list_file'],'r') as stream:
			users = yaml.load(stream.read())
	except IOError as errstr:
		print('Can\'t load userlist: %s'% errstr)
		sys.exit(1)

	sys.path.append(os.getcwd()+'/modules') 
	for f in os.listdir(os.getcwd()+'/modules'):
		name, ext = os.path.splitext(f)
		if ext == '.py':
			plugin = __import__(name)
			plugins[plugin]=plugin.Plugin(config)

	for username in users:
		user = None
		try:
			user = spwd.getspnam(username)
		except:
			print("Can\'t find user '%s' or permission denied" % username)
			continue 
		
		if user.sp_lstchg > 0 and user.sp_max > 0: # Check if password has expired.
			if (user.sp_lstchg + user.sp_max - user.sp_warn)*86400 < int(time.time()):
				for plug in plugins.values():
					if users[username].has_key(plug.__module__):
						plug.notify(message=config.get('password_expiration_text').format(USERNAME=username,HOSTNAME=servername), to=users[username].get(plug.__module__))

				
		if user.sp_expire > 0: # Check if account has expired.
			if int(time.time()) / 86400 >= user.sp_expire:
				for plug in plugins.values():
					if users[username].has_key(plug.__module__):
						plug.notify(message=config.get('account_expiration_text').format(USERNAME=username,HOSTNAME=servername), to=users[username].get(plug.__module__))

if __name__ == '__main__':
	main()

