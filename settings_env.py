import socket

"""
Check Enviroment
"""

DEV_HOST = ''
PROD_HOST = ''

if socket.gethostname() == DEV_HOST:
	from .settings_dev import *
elif socket.gethostname() == PROD_HOST:
	from .settings_prod import *
else:
	raise Exception("Cannot determine execution mode for host '%s'.  Please check DEV_HOST and PROD_HOST in settings_env.py." % node())