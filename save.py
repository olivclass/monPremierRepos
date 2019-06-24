#!/usr/bin/python
# -*-coding:Utf-8 -*-
### Creates a backup on a remote server of your website and its mysql database
#This script was created and tested in June 2019, on a Debian machine
#DATE 24/06/2019###



import subprocess
import os
import datetime
import time
import shutil
from datetime import datetime
from time import strftime

#Variable date:
d = datetime.now()
date = d.strftime("%d%m%y")

#web server's variables 
web = {
        'folder_wordpress' : '****',    #name of the directory containing the website on the local server
        'folder_backup' : '****',       #name of the directory which use for the backup 
        'wp_mysql_db' : '*****',        #name of the mysql database user 
        'wp_mysql_user' : '*****',      #name of the mysql database
        'wp_mysql_password' : '******', #password of the user account of the mysql database
}

dirName=web['folder_backup']

#backup server's variables
REMOTE = {
        'folder_ansible' : '*****',      #remote server backup directory
        'server' : '*****',              #Name of the remote machine for backup
        'user' : '*****',                #Username of the remote server account for the ssh connection

}


#creates the backup directory on the web server if it does not exist
if os.path.exists(dirName):
    print("backup directory", dirName , "exist")
else:
    os.mkdir(dirName)
    print("temporary backup folder of the web server", dirName , " create ")
#Backup of the mysql database in the folder on the web server
try:    
    os.system('mysqldump -u '+web['wp_mysql_user']+' -p'+web['wp_mysql_password']+' -d '+web['wp_mysql_db']+' > '+web['folder_backup']+'/wordpress-mysql'+date+'.sql')
except OSError as e: ## if failed, report it back to the user ##
    print('error encountered when saving the database',e)

#Backup of the website /var/www in the folder on the web server (web) 
try:
    print("folder compression started /var/www")
    os.system('tar -cf '+web['folder_backup']+'/www.tar '+web['folder_wordpress'])
  
except OSError as e: ## if failed, report it back to the user ##
    print('error encountered when saving website files',e)

#Backup of files on the remote server
os.system('rsync -vr '+web['folder_backup']+'/'' '+REMOTE['user']+'@'+REMOTE['server']+':'+REMOTE['folder_ansible'])
#Deletes the temporary backup directory on the web server
print("delete the temporary backup directory on the web server")
shutil.rmtree(dirName)

print('completed script') 

