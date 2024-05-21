# import OS module
from django.contrib.sessions.backends.db import SessionStore
import os
# Get the list of all files and directories
#path = "C://Users//Jorge//Downloads//material-dashboard-react-main//material-dashboard-react-main//backend//subdivions_db"
dirname = os.path.dirname(__file__)
filepath = os.path.join(dirname, '../subdivions_db')
dir_list = os.listdir(filepath)
#print("Files and directories in '", filepath, "' :")
# prints all files
#print(dir_list)
sep = "."
data_base_list = []
for l in dir_list:
    strip_db_number = l.split(sep, 1)[0]
    data_base_list.append(strip_db_number)
#print(data_base_list)

#dirname = os.path.dirname(__file__)
#filepath = os.path.join(dirname, 'material-dashboard-react-main/backend/subdivions_db')
#print(filename)


import datetime
s = SessionStore(session_key='2b1189a188b44ad18c35e113ac6ceead')
s['last_login'] = datetime.datetime(2005, 8, 20, 13, 35, 10)
s['last_login']
datetime.datetime(2005, 8, 20, 13, 35, 0)
s.save()